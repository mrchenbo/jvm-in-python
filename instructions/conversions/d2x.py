from instructions import base


class D2I (base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        d = stack.PopDouble()
        i = int(d)
        stack.PushInt(i)
# class D2L ( base.NoOperandsInstruction):
# class D2F ( base.NoOperandsInstruction):
