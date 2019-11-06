from .constant import readConstantPool
from .member import readMembers
from .attribute import readAttributes
from .attribute.attr_source_file import SourceFileAttribute

class ClassFile:
    def __init__(self):
        self.minorVersion = None
        self.majorVersion = None
        self.constantPool = None
        self.accessFlags = None
        self.thisClass = None
        self.superClass = None
        self.interfaces = None
        self.fields = None
        self.methods = None
        self.attributes = None

    def read(self, reader):
        self.readAndCheckMagic(reader)
        self.readAndCheckVersion(reader)
        self.constantPool = readConstantPool(reader)
        self.accessFlags = reader.readUint16()
        self.thisClass = reader.readUint16()
        self.superClass = reader.readUint16()
        self.interfaces = reader.readUint16s()
        self.fields = readMembers(reader, self.constantPool)  
        self.methods = readMembers(reader, self.constantPool)
        self.attributes = readAttributes(reader, self.constantPool)

    def readAndCheckMagic(self, reader):
        magic = reader.readUint32()
        if magic != 0xCAFEBABE:
            raise Exception(
                "java.lang.ClassFormatError: magic! {0}".fromat(magic))

    def readAndCheckVersion(self, reader):
        self.minorVersion = reader.readUint16()
        self.majorVersion = reader.readUint16()

        if self.majorVersion == 45:
            return
        elif self.majorVersion in (46, 47, 48, 49, 50, 51, 52) and self.minorVersion == 0:
            return

        raise Exception("ava.lang.UnsupportedClassVersionError!")

    def getMajorVersion(self):
        return self.majorVersion
    
    def getMinorVersion(self):
        return self.minorVersion

    def ConstantPool(self):
        return self.constantPool

    def getAccessFlags(self):
        return self.accessFlags

    def ClassName(self):
        return self.constantPool.getClassName(self.thisClass)

    def SuperClassName(self):
        if self.superClass > 0:
            return self.constantPool.getClassName(self.superClass)
        return ""  # 只有java.lang.Object没有超类

    def InterfaceNames(self):
        interfaceNames = []
        for inter in self.interfaces:
            interfaceNames.append(self.constantPool.getClassName(inter))
        return interfaceNames

    def Fields(self):
        return self.fields

    def Methods(self):
        return self.methods
    
    def AccessFlags(self):
        return self.accessFlags

    def SourceFileAttribute(self):
        for attrInfo in self.attributes:
            if isinstance(attrInfo, SourceFileAttribute):
                return attrInfo

        return None
 