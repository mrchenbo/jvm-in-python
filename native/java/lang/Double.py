import native
import struct

jlDouble = "java/lang/Double"


def doubleToRawLongBits(frame):
    value = frame.LocalVars().GetDouble(0)
    bits = struct.unpack(">q", struct.pack('>d', value))[0]
    frame.OperandStack().PushLong(bits)

def longBitsToDouble(frame):
    bits = frame.LocalVars().GetLong(0)
    value = struct.unpack(">d", struct.pack('>q', bits))[0]
    frame.OperandStack().PushDouble(value)


native.Register(jlDouble, "doubleToRawLongBits", "(D)J", doubleToRawLongBits)
native.Register(jlDouble, "longBitsToDouble", "(J)D", longBitsToDouble)
