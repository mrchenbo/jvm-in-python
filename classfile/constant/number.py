class ConstantIntegerInfo:
    def __init__(self):
        self.val = None

    def readInfo(self, reader):
        self.val = reader.readUint32()
    
    def Value(self):
        return self.val


class ConstantFloatInfo:
    def __init__(self):
        self.val = None

    def readInfo(self, reader):
        self.val = reader.readFloat()

    def Value(self):
        return self.val


class ConstantLongInfo:
    def __init__(self):
        self.val = None

    def readInfo(self, reader):
        self.val = reader.readUint64()

    def Value(self):
	    return self.val


class ConstantDoubleInfo:
    def __init__(self):
        self.val = None

    def readInfo(self, reader):
        self.val = reader.readDouble()

    def Value(self):
        return self.val
