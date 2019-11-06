from instructions import base
from rtda import heap


class LDC(base.Index8Instruction):
    def Execute(self, frame):
        _ldc(frame, self.Index)


class LDC_W(base.Index16Instruction):
    def Execute(self, frame):
        _ldc(frame, self.Index)


class LDC2_W(base.Index16Instruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        cp = frame.Method().Class().ConstantPool()
        c = cp.GetConstant(self.Index)

        if isinstance(c, int):
            stack.PushLong(c)
        elif isinstance(c, float):
            stack.PushDouble(c)
        else:
            raise Exception("java.lang.ClassFormatError")


def _ldc(frame, index):
    stack = frame.OperandStack()
    clazz = frame.Method().Class()
    cp = clazz.ConstantPool()
    c = cp.GetConstant(index)

    if isinstance(c, int):
        stack.PushInt(c)
    elif isinstance(c, float):
        stack.PushFloat(c)
    elif isinstance(c, str):
        internedStr = heap.JString(clazz.Loader(), c)
        stack.PushRef(internedStr)
    elif isinstance(c, heap.ClassRef):
        classRef = c
        classObj = classRef.ResolvedClass().JClass()
        stack.PushRef(classObj)
    else:
        raise Exception("todo: ldc!")
