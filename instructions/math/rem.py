from instructions import base


class DREM (base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        v2 = stack.PopDouble()
        v1 = stack.PopDouble()
        result = v1 % v2
        stack.PushDouble(result)


class FREM (base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        v2 = stack.PopFloat()
        v1 = stack.PopFloat()
        result = v1 % v2
        stack.PushDouble(result)


class IREM (base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        v2 = stack.PopInt()
        v1 = stack.PopInt()
        result = v1 % v2
        stack.PushInt(result)


class LREM (base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        v2 = stack.PopLong()
        v1 = stack.PopLong()
        result = v1 % v2
        stack.PushDouble(result)
