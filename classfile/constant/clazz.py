class ConstantClassInfo:
    def __init__(self, cp):
        self.cp = cp
        self.nameIndex = None

    def readInfo(self, reader):
        self.nameIndex = reader.readUint16()

    def Name(self):
        return self.cp.getUtf8(self.nameIndex)


class ConstantMemberrefInfo:
    def __init__(self, cp):
        self.cp = cp
        self.classIndex = None
        self.nameAndTypeIndex = None

    def readInfo(self, reader):
        self.classIndex = reader.readUint16()
        self.nameAndTypeIndex = reader.readUint16()

    def ClassName(self):
        return self.cp.getClassName(self.classIndex)

    def NameAndDescriptor(self):
        return self.cp.getNameAndType(self.nameAndTypeIndex)


class ConstantFieldrefInfo(ConstantMemberrefInfo):
    pass


class ConstantMethodrefInfo(ConstantMemberrefInfo):
    pass


class ConstantInterfaceMethodrefInfo(ConstantMemberrefInfo):
    pass
