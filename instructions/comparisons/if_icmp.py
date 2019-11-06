from instructions import base


class IF_ICMPEQ (base.BranchInstruction):
    def Execute(self, frame):
        val1, val2 = _icmpPop(frame)
        if val1 == val2:
                base.Branch(frame, self.Offset)


class IF_ICMPNE (base.BranchInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        val2 = stack.PopInt()
        val1 = stack.PopInt()
        if val1 != val2:
            base.Branch(frame, self.Offset)


class IF_ICMPLT (base.BranchInstruction):
    def Execute(self, frame):
        val1, val2 = _icmpPop(frame)
        if val1 < val2:
            base.Branch(frame, self.Offset)


class IF_ICMPLE (base.BranchInstruction):
    def Execute(self, frame):
        val1, val2 = _icmpPop(frame)
        if val1 <= val2:
            base.Branch(frame, self.Offset)


class IF_ICMPGT (base.BranchInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        val2 = stack.PopInt()
        val1 = stack.PopInt()
        if val1 > val2:
            base.Branch(frame, self.Offset)


class IF_ICMPGE (base.BranchInstruction):
    def Execute(self, frame):
        val1, val2 = _icmpPop(frame)
        if val1 >= val2:
            base.Branch(frame, self.Offset)


def _icmpPop(frame):
    stack = frame.OperandStack()
    val2 = stack.PopInt()
    val1 = stack.PopInt()
    return val1, val2
