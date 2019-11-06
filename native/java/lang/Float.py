import native
import struct


def floatToRawIntBits(frame):
    value = frame.LocalVars().GetFloat(0)
    bits = struct.unpack(">i", struct.pack('!f', value))[0]
    frame.OperandStack().PushInt(bits)


native.Register("java/lang/Float",
                "floatToRawIntBits", "(F)I", floatToRawIntBits)
