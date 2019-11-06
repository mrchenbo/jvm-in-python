from instructions import base


class ACONST_NULL (base.NoOperandsInstruction):
    def Execute(self, frame):
        frame.OperandStack().PushRef(None)


class DCONST_0 (base.NoOperandsInstruction):
    def Execute(self, frame):
        frame.OperandStack().PushRef(0.0)


class DCONST_1 (base.NoOperandsInstruction):
    def Execute(self, frame):
        frame.OperandStack().PushRef(1.0)


class FCONST_0 (base.NoOperandsInstruction):
    def Execute(self, frame):
        frame.OperandStack().PushRef(0.0)


class FCONST_1 (base.NoOperandsInstruction):
    def Execute(self, frame):
        frame.OperandStack().PushRef(1.0)


class FCONST_2 (base.NoOperandsInstruction):
    def Execute(self, frame):
        frame.OperandStack().PushRef(2.0)


class ICONST_M1 (base.NoOperandsInstruction):
    def Execute(self, frame):
        frame.OperandStack().PushRef(-1)


class ICONST_0 (base.NoOperandsInstruction):
    def Execute(self, frame):
        frame.OperandStack().PushRef(0)


class ICONST_1 (base.NoOperandsInstruction):
    def Execute(self, frame):
        frame.OperandStack().PushRef(1)


class ICONST_2 (base.NoOperandsInstruction):
    def Execute(self, frame):
        frame.OperandStack().PushRef(2)


class ICONST_3 (base.NoOperandsInstruction):
    def Execute(self, frame):
        frame.OperandStack().PushRef(3)


class ICONST_4 (base.NoOperandsInstruction):
    def Execute(self, frame):
        frame.OperandStack().PushRef(4)


class ICONST_5 (base.NoOperandsInstruction):
    def Execute(self, frame):
        frame.OperandStack().PushRef(5)


class LCONST_0 (base.NoOperandsInstruction):
    def Execute(self, frame):
        frame.OperandStack().PushRef(0)


class LCONST_1 (base.NoOperandsInstruction):
    def Execute(self, frame):
        frame.OperandStack().PushRef(1)
