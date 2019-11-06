from instructions import base


def _iload(frame, index):
    val = frame.LocalVars().GetInt(index)
    frame.OperandStack().PushInt(val)


class ILOAD (base.Index8Instruction):
    def Execute(self, frame):
        _iload(frame, self.Index)


class ILOAD_0 (base.NoOperandsInstruction):
    def Execute(self, frame):
        _iload(frame, 0)


class ILOAD_1 (base.NoOperandsInstruction):
    def Execute(self, frame):
        _iload(frame, 1)


class ILOAD_2 (base.NoOperandsInstruction):
    def Execute(self, frame):
        _iload(frame, 2)


class ILOAD_3 (base.NoOperandsInstruction):
    def Execute(self, frame):
        _iload(frame, 3)
