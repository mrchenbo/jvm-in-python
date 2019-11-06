from instructions import base


class IFEQ (base.BranchInstruction):
    def Execute(self, frame):
        val = frame.OperandStack().PopInt()
        if val == 0:
            base.Branch(frame, self.Offset)


class IFNE (base.BranchInstruction):
    def Execute(self, frame):
        val = frame.OperandStack().PopInt()
        if val != 0:
            base.Branch(frame, self.Offset)


# class IFLT ( base.BranchInstruction ):
class IFLE (base.BranchInstruction):
    def Execute(self, frame):
        val = frame.OperandStack().PopInt()
        if val <= 0:
            base.Branch(frame, self.Offset)


class IFGT (base.BranchInstruction):
    def Execute(self, frame):
        val = frame.OperandStack().PopInt()
        if val > 0:
            base.Branch(frame, self.Offset)


class IFGE (base.BranchInstruction):
    def Execute(self, frame):
        val = frame.OperandStack().PopInt()
        if val >= 0:
            base.Branch(frame, self.Offset)
