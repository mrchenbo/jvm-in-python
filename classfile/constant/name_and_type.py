class ConstantNameAndTypeInfo:
    def __init__(self):
        self.nameIndex = None
        self.descriptorIndex = None

    def readInfo(self, reader):
        self.nameIndex = reader.readUint16()
        self.descriptorIndex = reader.readUint16()
