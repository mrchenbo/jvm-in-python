from instructions import base

# Divide double


class DDIV(base.NoOperandsInstruction):

    def Execute(self, frame):
        stack = frame.OperandStack()
        v2 = stack.PopDouble()
        v1 = stack.PopDouble()
        result = v1 / v2
        stack.PushDouble(result)


# Divide float
class FDIV(base.NoOperandsInstruction):

    def Execute(self, frame):
        stack = frame.OperandStack()
        v2 = stack.PopFloat()
        v1 = stack.PopFloat()
        result = v1 / v2
        stack.PushFloat(result)


# Divide int
class IDIV(base.NoOperandsInstruction):

    def Execute(self, frame):
        stack = frame.OperandStack()
        v2 = stack.PopInt()
        v1 = stack.PopInt()
        if v2 == 0:
            raise Exception("java.lang.ArithmeticException: / by zero")

        result = int(v1 / v2)
        stack.PushInt(result)


# Divide long
class LDIV(base.NoOperandsInstruction):

    def Execute(self, frame):
        stack = frame.OperandStack()
        v2 = stack.PopLong()
        v1 = stack.PopLong()
        if v2 == 0:
            raise Exception("java.lang.ArithmeticException: / by zero")

        result = v1 / v2
        stack.PushLong(result)
