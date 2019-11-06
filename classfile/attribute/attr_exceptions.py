class ExceptionsAttribute:
    def __init__(self):
        self.exceptionIndexTable = None

    def readInfo(self, reader):
        self.exceptionIndexTable = reader.readUint16s()

    def exceptionIndexTable():
        return self.exceptionIndexTable
