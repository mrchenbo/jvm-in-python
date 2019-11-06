import classfile
from .clazz import newClass, Class
from .slots import newSlots
from .access_flags import *
from .class_name_helper import primitiveTypes
from rtda import heap


class ClassLoader:
    def __init__(self, cp, classMap):
        self.cp = cp
        self.classMap = classMap

    def LoadClass(self, name):
        if name in self.classMap:
            return self.classMap[name]

        if name[0] == '[':
            clazz = self.loadArrayClass(name)
        else:
            clazz = self.loadNonArrayClass(name)

        if "java/lang/Class" in self.classMap:
            jlClassClass = self.classMap["java/lang/Class"]
            clazz.jClass = jlClassClass.NewObject()
            clazz.jClass.extra = clazz

        return clazz

    def loadArrayClass(self, name):
        clazz = Class()

        clazz.accessFlags = ACC_PUBLIC
        clazz.name = name
        clazz.loader = self
        clazz.initStarted = True
        clazz.superClass = self.LoadClass("java/lang/Object")
        clazz.interfaces = [
            self.LoadClass("java/lang/Cloneable"),
            self.LoadClass("java/io/Serializable"),
        ]

        self.classMap[name] = clazz
        return clazz

    def loadNonArrayClass(self, name):
        data, entry = self.readClass(name)
        clazz = self.defineClass(data)
        link(clazz)
        # print("[Loaded %s from %s]" % (name, entry))
        return clazz

    def readClass(self, name):
        data, entry, err = self.cp.ReadClass(name)
        if err:
            raise ClassNotFoundException(name)
        return data, entry

    def defineClass(self, data):
        clazz = parseClass(data)
        clazz.loader = self
        resolveSuperClass(clazz)
        resolveInterfaces(clazz)
        self.classMap[clazz.name] = clazz
        return clazz

    def loadBasicClasses(self):
        jlClassClass = self.LoadClass("java/lang/Class")
        for name, clazz in self.classMap.items():
            if clazz.jClass == None:
                clazz.jClass = jlClassClass.NewObject()
                clazz.jClass.extra = clazz

    def loadPrimitiveClasses(self):
        for primitiveType in primitiveTypes:
            self.loadPrimitiveClass(primitiveType)

    def loadPrimitiveClass(self, className):
        clazz = Class()

        clazz.accessFlags = ACC_PUBLIC
        clazz.name = className
        clazz.loader = self
        clazz.initStarted = True

        clazz.jClass = self.classMap["java/lang/Class"].NewObject()
        clazz.jClass.extra = clazz
        self.classMap[className] = clazz


def NewClassLoader(cp):
    loader = ClassLoader(cp, {})
    loader.loadBasicClasses()
    loader.loadPrimitiveClasses()
    return loader


def parseClass(data):
    cf = classfile.Parse(data)
    return newClass(cf)


def resolveSuperClass(clazz):
    if clazz.name != "java/lang/Object":
        clazz.superClass = clazz.loader.LoadClass(clazz.superClassName)


def resolveInterfaces(clazz):
    interfaceCount = len(clazz.interfaceNames)
    if interfaceCount > 0:
        clazz.interfaces = [None] * interfaceCount
        for i, interfaceName in enumerate(clazz.interfaceNames):
            clazz.interfaces[i] = clazz.loader.LoadClass(interfaceName)


def link(clazz):
    verify(clazz)
    prepare(clazz)


def verify(clazz):
    pass


def prepare(clazz):
    calcInstanceFieldSlotIds(clazz)
    calcStaticFieldSlotIds(clazz)
    allocAndInitStaticVars(clazz)


def calcInstanceFieldSlotIds(clazz):
    slotId = 0
    if clazz.superClass != None:
        slotId = clazz.superClass.instanceSlotCount

    for field in clazz.fields:
        if not field.IsStatic():
            field.slotId = slotId
            slotId += 1
            if field.isLongOrDouble():
                slotId += 1

    clazz.instanceSlotCount = slotId


def calcStaticFieldSlotIds(clazz):
    slotId = 0
    for field in clazz.fields:
        if field.IsStatic():
            field.slotId = slotId
            slotId += 1
            if field.isLongOrDouble():
                slotId += 1

    clazz.staticSlotCount = slotId


def allocAndInitStaticVars(clazz):
    clazz.staticVars = newSlots(clazz.staticSlotCount)
    for field in clazz.fields:
        if field.IsStatic() and field.IsFinal():
            initStaticFinalVar(clazz, field)


def initStaticFinalVar(clazz, field):
    varbs = clazz.staticVars
    cp = clazz.constantPool
    cpIndex = field.ConstValueIndex()
    slotId = field.SlotId()

    if cpIndex > 0:
        if field.Descriptor() in ("Z", "B", "C", "S", "I"):
            val = cp.GetConstant(cpIndex)
            varbs.SetInt(slotId, val)
        elif field.Descriptor() == 'J':
            val = cp.GetConstant(cpIndex)
            varbs.SetLong(slotId, val)
        elif field.Descriptor() == 'F':
            val = cp.GetConstant(cpIndex)
            varbs.SetFloat(slotId, val)
        elif field.Descriptor() == 'D':
            val = cp.GetConstant(cpIndex)
            varbs.SetDouble(slotId, val)
        elif field.Descriptor() == 'Ljava/lang/String;':
            goStr = cp.GetConstant(cpIndex)
            jStr = heap.JString(clazz.Loader(), goStr)
            varbs.SetRef(slotId, jStr)
