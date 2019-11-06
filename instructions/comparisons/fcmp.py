from instructions import base


def _fcmp(frame, gFlag):
    stack = frame.OperandStack()
    v2 = stack.PopFloat()
    v1 = stack.PopFloat()
    if v1 > v2:
        stack.PushInt(1)
    elif v1 == v2:
        stack.PushInt(0)
    elif v1 < v2:
        stack.PushInt(-1)
    elif gFlag:
        stack.PushInt(1)
    else:
        stack.PushInt(-1)


class FCMPG (base.NoOperandsInstruction):
    def Execute(self, frame):
        _fcmp(frame, True)


class FCMPL (base.NoOperandsInstruction):
    def Execute(self, frame):
        _fcmp(frame, False)
