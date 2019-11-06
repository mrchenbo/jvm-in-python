class ConstantUtf8Info:
    def __init__(self):
        self.str = None

    def readInfo(self, reader):
        length = reader.readUint16()
        byte = reader.readBytes(length)
        self.str = byte.decode(encoding='utf-8')

class ConstantStringInfo:
    def __init__(self, cp):
        self.cp = cp
        self.stringIndex = None

    def readInfo(self, reader):
        self.stringIndex = reader.readUint16()

    def __str__(self):
        return self.cp.getUtf8(self.stringIndex)

    def String(self):
        return self.__str__()
     