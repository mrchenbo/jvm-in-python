class UnparsedAttribute:
    def __init__(self, name, length, info):
        self.name = name
        self.length = length
        self.info = info

    def readInfo(self, reader):
        self.info = reader.readBytes(self.length)
