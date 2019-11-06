from instructions import base


class DSUB(base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        v2 = stack.PopDouble()
        v1 = stack.PopDouble()
        result = v1 - v2
        stack.PushDouble(result)


class FSUB(base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        v2 = stack.PopFloat()
        v1 = stack.PopFloat()
        result = v1 - v2
        stack.PushFloat(result)


class ISUB(base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        v2 = stack.PopInt()
        v1 = stack.PopInt()
        result = v1 - v2
        stack.PushInt(result)


class LSUB(base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        v2 = stack.PopLong()
        v1 = stack.PopLong()
        result = v1 - v2
        stack.PushLong(result)
