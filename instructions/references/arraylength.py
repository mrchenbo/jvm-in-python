from instructions import base

class ARRAY_LENGTH(base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        arrRef = stack.PopRef()
        if arrRef == None:
            raise Exception("java.lang.NullPointerException")

        arrLen = arrRef.ArrayLength()
        stack.PushInt(arrLen)