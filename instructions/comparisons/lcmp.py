from instructions import base


class LCMP (base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        v2 = stack.PopLong()
        v1 = stack.PopLong()
        if v1 > v2:
            stack.PushInt(1)
        elif v1 == v2:
            stack.PushInt(0)
        else:
            stack.PushInt(-1)
