from instructions import base

# Load float from local variable


class FLOAD(base.Index8Instruction):
    def Execute(self, frame):
        _fload(frame, self.Index)


class FLOAD_0(base.NoOperandsInstruction):

    def Execute(self, frame):
        _fload(frame, 0)


class FLOAD_1(base.NoOperandsInstruction):

    def Execute(self, frame):
        _fload(frame, 1)


class FLOAD_2(base.NoOperandsInstruction):

    def Execute(self, frame):
        _fload(frame, 2)


class FLOAD_3(base.NoOperandsInstruction):

    def Execute(self, frame):
        _fload(frame, 3)


def _fload(frame, index):
    val = frame.LocalVars().GetFloat(index)
    frame.OperandStack().PushFloat(val)
