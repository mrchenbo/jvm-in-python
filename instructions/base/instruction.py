

class Instruction:
    def FetchOperands(self, reader):
        raise NotImplementedError

    def Execute(self, frame):
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__


class NoOperandsInstruction(Instruction):
    def FetchOperands(self, reader):
        pass

class BranchInstruction(Instruction):
    def FetchOperands(self, reader):
        self.Offset = reader.ReadInt16()

class Index8Instruction(Instruction):
    def FetchOperands(self, reader):
        self.Index = reader.ReadInt8()

class Index16Instruction(Instruction):
    def FetchOperands(self, reader):
        self.Index = reader.ReadInt16()