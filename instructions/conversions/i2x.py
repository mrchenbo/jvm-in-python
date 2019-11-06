from struct import pack, unpack
from instructions import base 
# Convert int to byte
class I2B(base.NoOperandsInstruction):

    def Execute(self, frame):
        stack = frame.OperandStack()
        i = stack.PopInt()
        b = _ito(i, ">b")
        stack.PushInt(b)


# Convert int to char
class I2C(base.NoOperandsInstruction):

    def Execute(self, frame):
        stack = frame.OperandStack()
        i = stack.PopInt()
        c = _ito(i, '>c')
        stack.PushInt(c)


# Convert int to short
class I2S(base.NoOperandsInstruction):

    def Execute(self, frame):
        stack = frame.OperandStack()
        i = stack.PopInt()
        s = _ito(i, '>h')
        stack.PushInt(s)


# Convert int to long
class I2L(base.NoOperandsInstruction):

    def Execute(self, frame):
        stack = frame.OperandStack()
        i = stack.PopInt()
        l = int(i)
        stack.PushLong(l)


# Convert int to float
class I2F(base.NoOperandsInstruction):

    def Execute(self, frame):
        stack = frame.OperandStack()
        i = stack.PopInt()
        f = _ito(i, '>f')
        stack.PushFloat(f)


# Convert int to double
class I2D(base.NoOperandsInstruction):

    def Execute(self, frame):
        stack = frame.OperandStack()
        i = stack.PopInt()
        d = _ito(i, ">d")
        stack.PushDouble(d)

def _ito(input, format):
    return unpack(format, pack('>i', input))[0]
