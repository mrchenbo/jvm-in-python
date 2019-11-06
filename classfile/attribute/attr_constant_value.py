class ConstantValueAttribute:
    def readInfo(self, reader):
        self.constantValueIndex = reader.readUint16()

    def ConstantValueIndex(self):
        return self.constantValueIndex
