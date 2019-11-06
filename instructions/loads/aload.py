from instructions import base


class ALOAD(base.Index8Instruction):

    def Execute(self, frame):
        _aload(frame, self.Index)


class ALOAD_0(base.NoOperandsInstruction):

    def Execute(self, frame):
        _aload(frame, 0)


class ALOAD_1(base.NoOperandsInstruction):

    def Execute(self, frame):
        _aload(frame, 1)


class ALOAD_2(base.NoOperandsInstruction):

    def Execute(self, frame):
        _aload(frame, 2)


class ALOAD_3(base.NoOperandsInstruction):

    def Execute(self, frame):
        _aload(frame, 3)


def _aload(frame, index):
    ref = frame.LocalVars().GetRef(index)
    frame.OperandStack().PushRef(ref)
