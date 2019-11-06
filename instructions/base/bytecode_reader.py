from struct import *

class BytecodeReader:
    def __init__(self):
        pass

    def Reset(self, code, pc):
        self.code = code
        self.pc = pc

    def ReadUint8(self):
        val = unpack(">B", self.code[self.pc:self.pc+1])[0]
        self.pc += 1
        return val

    def ReadInt8(self):
        val = unpack(">b", self.code[self.pc:self.pc+1])[0]
        self.pc += 1
        return val

    def ReadUint16(self):
        val = unpack(">H", self.code[self.pc: self.pc+2])[0]
        self.pc += 2
        return val

    def ReadInt16(self):
        val = unpack(">h", self.code[self.pc: self.pc+2])[0]
        self.pc += 2
        return val

    def readInt32(self):
        val = unpack(">l", self.data[self.pc: self.pc+4])[0]
        self.pc += 4
        return val

    def PC(self):
        return self.pc
