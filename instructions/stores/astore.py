from instructions import base

class ASTORE(base.Index8Instruction):

    def Execute(self, frame):
	    _astore(frame, self.Index)


class ASTORE_0(base.NoOperandsInstruction):

    def Execute(self, frame):
	    _astore(frame, 0)


class ASTORE_1(base.NoOperandsInstruction):

    def Execute(self, frame):
	    _astore(frame, 1)


class ASTORE_2(base.NoOperandsInstruction):

    def Execute(self, frame):
	    _astore(frame, 2)


class ASTORE_3(base.NoOperandsInstruction):

    def Execute(self, frame):
	    _astore(frame, 3)


def _astore(frame, index):
	ref = frame.OperandStack().PopRef()
	frame.LocalVars().SetRef(index, ref)
