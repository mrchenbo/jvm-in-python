from instructions import base


class IAND (base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        v2 = stack.PopInt()
        v1 = stack.PopInt()
        result = v1 & v2
        stack.PushInt(result)


class LAND (base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        v2 = stack.PopLong()
        v1 = stack.PopLong()
        result = v1 & v2
        stack.PushLong(result)
