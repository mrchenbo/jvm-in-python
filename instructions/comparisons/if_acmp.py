from instructions import base


class IF_ACMPEQ (base.BranchInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        ref2 = stack.PopRef()
        ref1 = stack.PopRef()
        if ref1 == ref2:
            base.Branch(frame, self.Offset)


class IF_ACMPNE (base.BranchInstruction):
    def Execute(self, frame):
        if not _acmp(frame):
            base.Branch(frame, self.Offset)


def _acmp(frame):
    stack = frame.OperandStack()
    ref2 = stack.PopRef()
    ref1 = stack.PopRef()
    return ref1 == ref2
