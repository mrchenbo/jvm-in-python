from .class_member import ClassMember
from .method_descriptor_parser import parseMethodDescriptor
from .exception_table import newExceptionTable


class Method(ClassMember):
    def __init__(self):
        super().__init__()
        self.maxStack = 0
        self.maxLocals = 0
        self.argSlotCount = 0
        self.code = None
        self.exceptionTable = None
        self.lineNumberTable = None

    def copyAttributes(self, cfMethod):
        codeAttr = cfMethod.CodeAttribute()
        if codeAttr != None:
            self.maxStack = codeAttr.MaxStack()
            self.maxLocals = codeAttr.MaxLocals()
            self.code = codeAttr.Code()
            self.lineNumberTable = codeAttr.LineNumberTableAttribute()
            self.exceptionTable = newExceptionTable(
                codeAttr.ExceptionTable(), self.clazz.constantPool)

    def calcArgSlotCount(self, paramTypes):
        for paramType in paramTypes:
            self.argSlotCount += 1

        if not self.IsStatic():
            self.argSlotCount += 1

    def MaxLocals(self):
        return self.maxLocals

    def MaxStack(self):
        return self.maxStack

    def ArgSlotCount(self):
        return self.argSlotCount

    def Code(self):
        return self.code

    def injectCodeAttribute(self, returnType):
        self.maxStack = 4
        self.maxLocals = self.argSlotCount
        rt = returnType[0]

        if rt == 'V':
            self.code = b'\xfe\xb1'  # return
        elif rt == 'D':
            self.code = b'\xfe\xaf'  # dreturn
        elif rt == 'F':
            self.code = b'\xfe\xae'  # freturn
        elif rt == 'J':
            self.code = b'\xfe\xad'  # lreturn
        elif rt in ('L', '['):
            self.code = b'\xfe\xb0'  # areturn
        else:
            self.code = b'\xfe\xac'  # ireturn

    def FindExceptionHandler(self, exClass, pc):
        handler = self.exceptionTable.findExceptionHandler(exClass, pc)
        if handler != None:
            return handler.handlerPc
        else:
            return -1

    def GetLineNumber(self, pc):
        if self.IsNative():
            return -2

        if self.lineNumberTable == None:
            return -1

        return self.lineNumberTable.GetLineNumber(pc)


def newMethods(clazz, cfMethods):
    methods = [None] * len(cfMethods)
    for i, cfMethod in enumerate(cfMethods):
        methods[i] = newMethod(clazz, cfMethod)

    return methods


def newMethod(clazz, cfMethod):
    method = Method()
    method.clazz = clazz
    method.copyMemberInfo(cfMethod)
    method.copyAttributes(cfMethod)
    md = parseMethodDescriptor(method.descriptor)
    method.calcArgSlotCount(md.parameterTypes)
    if method.IsNative():
        method.injectCodeAttribute(md.returnType)

    return method
