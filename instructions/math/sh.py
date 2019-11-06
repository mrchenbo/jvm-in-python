from instructions import base


class ISHL (base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        v2 = stack.PopInt()
        v1 = stack.PopInt()
        s = v2 & 0x1f
        result = v1 << s
        stack.PushInt(result)


class ISHR (base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        v2 = stack.PopInt()
        v1 = stack.PopLong()
        s = v2 & 0x1f
        result = v1 << s
        stack.PushLong(result)


class IUSHR (base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        v2 = stack.PopInt()
        v1 = stack.PopInt()
        result = v1 >> v2
        stack.PushInt(result)


class LSHL (base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        v2 = stack.PopInt()
        v1 = stack.PopLong()
        s = v2 & 0x3f
        result = v1 << s
        stack.PushLong(result)

# class LSHR ( base.NoOperandsInstruction ):
# class LUSHR ( base.NoOperandsInstruction ):
