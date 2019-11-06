from instructions import base


def _lstore(frame, index):
    val = frame.OperandStack().PopLong()
    frame.LocalVars().SetLong(index, val)


class LSTORE (base.Index8Instruction):
    def Execute(self, frame):
        _lstore(frame, self.Index)


class LSTORE_0 (base.NoOperandsInstruction):
    def Execute(self, frame):
        _lstore(frame, 0)


class LSTORE_1 (base.NoOperandsInstruction):
    def Execute(self, frame):
        _lstore(frame, 1)


class LSTORE_2 (base.NoOperandsInstruction):
    def Execute(self, frame):
        _lstore(frame, 2)


class LSTORE_3 (base.NoOperandsInstruction):
    def Execute(self, frame):
        _lstore(frame, 3)
