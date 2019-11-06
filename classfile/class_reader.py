from struct import *


class ClassReader:
    def __init__(self, data):
        self.data = data

    def readUint8(self):
        val = unpack(">B", self.data[0:1])[0]
        self.data = self.data[1:]
        return val

    def readUint16(self):
        val = unpack(">H", self.data[:2])[0]
        # val = int.from_bytes(self.data[:2], byteorder='big', signed=False)
        self.data = self.data[2:]
        return val

    def readUint32(self):
        val = unpack(">L", self.data[:4])[0]
        self.data = self.data[4:]
        return val

    def readUint64(self):
        val = unpack(">Q", self.data[:8])[0]
        self.data = self.data[8:]
        return val

    def readUint16s(self):
        n = self.readUint16()
        s = []
        for i in range(n):
            s.append(self.readUint16())
        return s

    def readFloat(self):
        val = unpack(">f", self.data[:4])[0]
        self.data = self.data[4:]
        return val

    def readDouble(self):
        val = unpack(">d", self.data[:8])[0]
        self.data = self.data[8:]
        return val

    def readBytes(self, n):
        byte = self.data[:n]
        self.data = self.data[n:]
        return byte
