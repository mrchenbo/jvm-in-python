from instructions import base


def _istore(frame, index):
    val = frame.OperandStack().PopInt()
    frame.LocalVars().SetInt(index, val)


class ISTORE(base.Index8Instruction):
    def Execute(self, frame):
        _istore(frame, self.Index)


class ISTORE_0 (base.NoOperandsInstruction):
    def Execute(self, frame):
        _istore(frame, 0)


class ISTORE_1 (base.NoOperandsInstruction):
    def Execute(self, frame):
        _istore(frame, 1)


class ISTORE_2 (base.NoOperandsInstruction):
    def Execute(self, frame):
        _istore(frame, 2)


class ISTORE_3 (base.NoOperandsInstruction):
    def Execute(self, frame):
        _istore(frame, 3)
