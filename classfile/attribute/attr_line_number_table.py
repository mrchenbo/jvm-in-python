class LineNumberTableAttribute:
    def __init__(self):
        self.lineNumberTable = None

    def readInfo(self, reader):
        lineNumberTableLength = reader.readUint16()
        self.lineNumberTable = []
        for i in range(lineNumberTableLength):
            self.lineNumberTable.append(LineNumberTableEntry(
                reader.readUint16(),
                reader.readUint16(),
            ))

    def GetLineNumber(self, pc):
        i = len(self.lineNumberTable) - 1
        while i >= 0:
            entry = self.lineNumberTable[i]
            if pc >= entry.startPc:
                return entry.lineNumber
            i -= 1
        return -1


class LineNumberTableEntry:
    def __init__(self, startPc, lineNumber):
        self.startPc = startPc
        self.lineNumber = lineNumber
