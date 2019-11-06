from .__init__ import readAttributes
from .attr_line_number_table import LineNumberTableAttribute


class CodeAttribute:
    def __init__(self, cp):
        self.cp = cp
        self.maxStack = None
        self.maxLocals = None
        self.code = None
        self.exceptionTable = None
        self.attributes = None

    def readInfo(self, reader):
        self.maxStack = reader.readUint16()
        self.maxLocals = reader.readUint16()
        codeLength = reader.readUint32()
        self.code = reader.readBytes(codeLength)
        self.exceptionTable = readExceptionTable(reader)
        self.attributes = readAttributes(reader, self.cp)

    def MaxLocals(self):
        return self.maxLocals

    def MaxStack(self):
        return self.maxStack

    def Code(self):
        return self.code

    def LineNumberTableAttribute(self):
        for attrInfo in self.attributes:
            if isinstance(attrInfo, LineNumberTableAttribute):
                return attrInfo

        return None

    def ExceptionTable(self):
        return self.exceptionTable


class ExceptionTableEntry:
    def __init__(self, startPc, endPc, handlerPc, catchType):
        self.startPc = startPc
        self.endPc = endPc
        self.handlerPc = handlerPc
        self.catchType = catchType

    def StartPc(self):
        return self.startPc

    def EndPc(self):
        return self.endPc

    def HandlerPc(self):
        return self.handlerPc

    def CatchType(self):
        return self.catchType


def readExceptionTable(reader):
    exceptionTableLength = reader.readUint16()
    exceptionTable = []
    for i in range(exceptionTableLength):
        exceptionTable.append(ExceptionTableEntry(reader.readUint16(
        ), reader.readUint16(), reader.readUint16(), reader.readUint16(),))

    return exceptionTable
