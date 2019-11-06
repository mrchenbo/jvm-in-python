from instructions import base
from instructions.base import checkNotNil, checkIndex


class AALOAD(base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        index = stack.PopInt()
        arrRef = stack.PopRef()
        checkNotNil(arrRef)
        refs = arrRef.Refs()
        checkIndex(len(refs), index)
        stack.PushRef(refs[index])


# class BALOAD(base.NoOperandsInstruction):
class CALOAD(base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        index = stack.PopInt()
        arrRef = stack.PopRef()

        checkNotNil(arrRef)
        chars = arrRef.Chars()
        checkIndex(len(chars), index)
        c = chars[index]
        if isinstance(c, str):
            c = ord(c)
        stack.PushInt(c)
# class DALOAD(base.NoOperandsInstruction):


class FALOAD(base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        index = stack.PopInt()
        arrRef = stack.PopRef()

        checkNotNil(arrRef)
        floats = arrRef.Floats()
        checkIndex(len(floats), index)
        stack.PushFloat(floats[index])


class IALOAD(base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        index = stack.PopInt()
        arrRef = stack.PopRef()

        checkNotNil(arrRef)
        ints = arrRef.Ints()
        checkIndex(len(ints), index)
        stack.PushInt(ints[index])

# class LALOAD(base.NoOperandsInstruction):
# class SALOAD(base.NoOperandsInstruction):
