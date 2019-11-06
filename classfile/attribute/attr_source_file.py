class SourceFileAttribute:
    def __init__(self, cp):
        self.cp = cp
        self.sourceFileIndex = None

    def readInfo(self, reader):
        self.sourceFileIndex = reader.readUint16()

    def FileName(self):
        return self.cp.getUtf8(self.sourceFileIndex)
