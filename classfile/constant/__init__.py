from enum import Enum

from .clazz import *
from .number import *
from .string import *
from .name_and_type import *
from .cp_invoke_dynamic import *

class Constant(Enum):
    Class = 7
    Fieldref = 9
    Methodref = 10
    InterfaceMethodref = 11
    String = 8
    Integer = 3
    Float = 4
    Long = 5
    Double = 6
    NameAndType = 12
    Utf8 = 1
    MethodHandle = 15
    MethodType = 16
    InvokeDynamic = 18


class ConstantPool:
    def __init__(self, cp):
        self.cp = cp

    def setConstant(self, index, constant):
        self.cp[index] = constant

    def getConstant(self, index):
        return self.cp[index]

    def getConstantInfo(self, index):
        cpInfo = self.cp[index]
        if cpInfo:
            return cpInfo

        raise Exception("Invalid constant pool index!")

    def getNameAndType(self, index):
        ntInfo = self.getConstantInfo(index)
        name = self.getUtf8(ntInfo.nameIndex)
        _type = self.getUtf8(ntInfo.descriptorIndex)
        return name, _type

    def getClassName(self, index):
        classInfo = self.getConstantInfo(index)
        return self.getUtf8(classInfo.nameIndex)

    def getUtf8(self, index):
        utf8Info = self.getConstantInfo(index)
        return utf8Info.str

    def __len__(self):
        return len(self.cp)


def readConstantPool(reader):
    cpCount = reader.readUint16()

    cp = ConstantPool([None] * cpCount)

    i = 1
    while i < cpCount:
        cp.setConstant(i, readConstantInfo(reader, cp))
        if isinstance(cp.getConstant(i), (ConstantLongInfo, ConstantDoubleInfo)):
            i += 2
        else:
            i += 1

    return cp


def readConstantInfo(reader, cp):
    tag = reader.readUint8()
    c = newConstantInfo(tag, cp)
    c.readInfo(reader)
    return c


def newConstantInfo(tag, cp):
    if tag == Constant.Integer.value:
        return ConstantIntegerInfo()
    elif tag == Constant.Float.value:
        return ConstantFloatInfo()
    elif tag == Constant.Long.value:
        return ConstantLongInfo()
    elif tag == Constant.Double.value:
        return ConstantDoubleInfo()
    elif tag == Constant.Utf8.value:
        return ConstantUtf8Info()
    elif tag == Constant.String.value:
        return ConstantStringInfo(cp)
    elif tag == Constant.Class.value:
        return ConstantClassInfo(cp)
    elif tag == Constant.Fieldref.value:
        return ConstantFieldrefInfo(cp)
    elif tag == Constant.Methodref.value:
        return ConstantMethodrefInfo(cp)
    elif tag == Constant.InterfaceMethodref.value:
        return ConstantInterfaceMethodrefInfo(cp)
    elif tag == Constant.NameAndType.value:
        return ConstantNameAndTypeInfo()
    elif tag == Constant.MethodType.value:
        return ConstantMethodTypeInfo()
    elif tag == Constant.MethodHandle.value:
        return ConstantMethodHandleInfo()
    elif tag == Constant.InvokeDynamic.value:
        return ConstantInvokeDynamicInfo()

    raise Exception("java.lang.ClassFormatError: constant pool tag!")
