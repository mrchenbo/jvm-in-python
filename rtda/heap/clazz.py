from .access_flags import *
from .object import newObject, Object
from .constant_pool import newConstantPool
from .field import newFields
from .method import newMethods
from .class_name_helper import *


class Class:
    def __init__(self):
        self.accessFlags = None
        self.name = None
        self.superClassName = None
        self.interfaceNames = None
        self.constantPool = None
        self.fields = None
        self.methods = []
        self.loader = None
        self.superClass = None
        self.interfaces = []
        self.instanceSlotCount = None
        self.staticSlotCount = None
        self.staticVars = None
        self.initStarted = False
        self.jClass = None
        self.sourceFile = None

    def IsPublic(self):
        return 0 != self.accessFlags & ACC_PUBLIC

    def IsFinal(self):
        return 0 != self.accessFlags & ACC_FINAL

    def IsSuper(self):
        return 0 != self.accessFlags & ACC_SUPER

    def IsInterface(self):
        return 0 != self.accessFlags & ACC_INTERFACE

    def IsAbstract(self):
        return 0 != self.accessFlags & ACC_ABSTRACT

    def IsSynthetic(self):
        return 0 != self.accessFlags & ACC_SYNTHETIC

    def IsAnnotation(self):
        return 0 != self.accessFlags & ACC_ANNOTATION

    def IsEnum(self):
        return 0 != self.accessFlags & ACC_ENUM

    def getPackageName(self):
        i = str.rfind(self.name, "/")
        if i >= 0:
            return self.name[:i]
        return ""

    def NewObject(self):
        return newObject(self)

    def isAccessibleTo(self, other):
        return self.IsPublic() or self.getPackageName() == other.getPackageName()

    def IsAssignableFrom(self, other):
        s, t = other, self
        if s == t:
            return True

        if not s.IsArray():
            if not s.IsInterface():
                if not t.IsInterface():
                    return s.IsSubClassOf(t)
                else:
                    return s.IsImplements(t)
            else:
                if not t.IsInterface():
                    return t.isJlObject()
                else:
                    return t.isSuperInterfaceOf(s)
        else:
            if not t.IsArray():
                if not t.IsInterface():
                    return t.isJlObject()
                else:
                    return t.isJlCloneable() or t.isJioSerializable()
            else:
                sc = s.ComponentClass()
                tc = t.ComponentClass()
                return sc == tc or tc.isAssignableFrom(sc)
        return False

    def IsSubClassOf(self, other):
        c = self.superClass
        while c is not None:
            if c == other:
                return True
            c = c.superClass

        return False

    def IsSuperClassOf(self, other):
        return other.IsSubClassOf(self)

    def IsImplements(self, iface):
        c = self
        while c is not None:
            for i in c.interfaces:
                if i == iface or i.isSubInterfaceOf(iface):
                    return True
            c = c.superClass

        return false

    def isSubInterfaceOf(self, iface):
        for superInterface in self.interfaces:
            if superInterface == iface or superInterface.isSubInterfaceOf(iface):
                return True

        return False

    def GetMainMethod(self):
        return self.getStaticMethod("main", "([Ljava/lang/String;)V")

    def GetClinitMethod(self):
        return self.getStaticMethod("<clinit>", "()V")

    def getStaticMethod(self, name, descriptor):
        for method in self.methods:
            if method.IsStatic() and method.name == name and method.descriptor == descriptor:
                return method
        return None

    def ConstantPool(self):
        return self.constantPool

    def StaticVars(self):
        return self.staticVars

    def Name(self):
        return self.name

    def SuperClass(self):
        return self.superClass

    def Loader(self):
        return self.loader

    def InitStarted(self):
        return self.initStarted

    def StartInit(self):
        self.initStarted = True

    def IsArray(self):
        return self.name[0] == '['

    def NewArray(self, count):
        if not self.IsArray():
            raise Exception("Not array class: " + self.name)

        name = self.Name()

        if name == "[Z":
            return Object(self, [None] * count)
        if name == "[B":
            return Object(self, [None] * count)
        if name == "[C":
            return Object(self, [None] * count)
        if name == "[S":
            return Object(self, [None] * count)
        if name == "[I":
            return Object(self, [None] * count)
        if name == "[J":
            return Object(self, [None] * count)
        if name == "[F":
            return Object(self, [None] * count)
        if name == "[D":
            return Object(self, [None] * count)
        return Object(self, [None] * count)

    def ArrayClass(self):
        arrayClassName = getArrayClassName(self.name)
        return self.loader.LoadClass(arrayClassName)

    def ComponentClass(self):
        componentClassName = getComponentClassName(self.name)
        return self.loader.LoadClass(componentClassName)

    def getField(self, name, descriptor, isStatic):
        c = self
        while c is not None:
            for field in c.fields:
                if field.IsStatic() == isStatic and \
                        field.name == name and field.descriptor == descriptor:
                    return field
            c = c.superClass
        return None

    def JavaName(self):
        return self.name.replace(".", "/")

    def JClass(self):
        return self.jClass

    def IsPrimitive(self):
        return self.name in primitiveTypes

    def GetPackageName(self):
        return self.getPackageName()

    def GetRefVar(self, fieldName, fieldDescriptor):
        field = self.getField(fieldName, fieldDescriptor, True)
        return self.staticVars.GetRef(field.slotId)

    def GetInstanceMethod(self, name, descriptor):
        return self.getMethod(name, descriptor, False)

    def getMethod(self, name, descriptor, isStatic):
        c = self
        while c is not None:
            for method in c.methods:
                if method.IsStatic() == isStatic and \
                        method.name == name and \
                        method.descriptor == descriptor:

                    return method

            c = c.superClass
        return None

    def SourceFile(self):
        return self.sourceFile

    def GetStaticMethod(self, name, descriptor):
	    return self.getMethod(name, descriptor, True)



def newClass(cf):
    clazz = Class()
    clazz.accessFlags = cf.AccessFlags()
    clazz.name = cf.ClassName()
    clazz.superClassName = cf.SuperClassName()
    clazz.interfaceNames = cf.InterfaceNames()
    clazz.constantPool = newConstantPool(clazz, cf.ConstantPool())
    clazz.fields = newFields(clazz, cf.Fields())
    clazz.methods = newMethods(clazz, cf.Methods())
    clazz.sourceFile = getSourceFile(cf)
    return clazz


def getSourceFile(cf):
    sfAttr = cf.SourceFileAttribute()
    
    if sfAttr != None:
        return sfAttr.FileName()

    return "Unknown"
