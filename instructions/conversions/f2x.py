from struct import pack, unpack
from instructions import base

# Convert float to double


class F2D(base.NoOperandsInstruction):

    def Execute(self, frame):
        stack = frame.OperandStack()
        f = stack.PopFloat()
        d = _fto(f, ">d")
        stack.PushDouble(d)


# Convert float to int
class F2I(base.NoOperandsInstruction):

    def Execute(self, frame):
        stack = frame.OperandStack()
        f = stack.PopFloat()
        i = _fto(f, ">i")
        stack.PushInt(i)


# Convert float to long
class F2L(base.NoOperandsInstruction):

    def Execute(self, frame):
        stack = frame.OperandStack()
        f = stack.PopFloat()
        l = _fto(f, ">q")
        stack.PushLong(l)

def _fto(input, format):
    return unpack(format, pack('>f', input))[0]