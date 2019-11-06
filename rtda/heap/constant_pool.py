import classfile
from .cp_classref import newClassRef
from .cp_fieldref import newFieldRef
from .cp_methodref import newMethodRef
from .cp_interface_methodref import newInterfaceMethodRef


class Constant:
    pass


class ConstantPool:
    def __init__(self, clazz, consts):
        self.clazz = clazz
        self.consts = consts

    def GetConstant(self, index):
        c = self.consts[index]
        if c is None:
            raise KeyError("No constants at index %d" % index)
        return c


def newConstantPool(clazz, cfCp):
    cpCount = len(cfCp)
    consts = [None] * cpCount
    rtCp = ConstantPool(clazz, consts)

    i = 1
    while i < cpCount:
        cpInfo = cfCp.getConstant(i)
        if isinstance(cpInfo, classfile.ConstantIntegerInfo):
            consts[i] = cpInfo.Value()
        elif isinstance(cpInfo, classfile.ConstantFloatInfo):
            consts[i] = cpInfo.Value()
        elif isinstance(cpInfo, classfile.ConstantLongInfo):
            consts[i] = cpInfo.Value()
            i += 1
        elif isinstance(cpInfo, classfile.ConstantDoubleInfo):
            consts[i] = cpInfo.Value()
            i += 1
        elif isinstance(cpInfo, classfile.ConstantStringInfo):
            consts[i] = cpInfo.String()
        elif isinstance(cpInfo, classfile.ConstantClassInfo):
            consts[i] = newClassRef(rtCp, cpInfo)
        elif isinstance(cpInfo, classfile.ConstantFieldrefInfo):
            consts[i] = newFieldRef(rtCp, cpInfo)
        elif isinstance(cpInfo, classfile.ConstantMethodrefInfo):
            consts[i] = newMethodRef(rtCp, cpInfo)
        elif isinstance(cpInfo, classfile.ConstantInterfaceMethodrefInfo):
            consts[i] = newInterfaceMethodRef(rtCp, cpInfo)
        
        i += 1

    return rtCp
