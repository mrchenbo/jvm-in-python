from instructions import base
from instructions.base import checkNotNil, checkIndex


class AASTORE(base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        ref = stack.PopRef()
        index = stack.PopInt()
        arrRef = stack.PopRef()

        checkNotNil(arrRef)
        refs = arrRef.Refs()
        checkIndex(len(refs), index)
        refs[index] = ref


# class BASTORE(base.NoOperandsInstruction):


class CASTORE(base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        val = stack.PopInt()
        index = stack.PopInt()
        arrRef = stack.PopRef()

        checkNotNil(arrRef)
        chars = arrRef.Chars()
        checkIndex(len(chars), index)
        chars[index] = val
# class DASTORE(base.NoOperandsInstruction):
# class FASTORE(base.NoOperandsInstruction):


class IASTORE(base.NoOperandsInstruction):

    def Execute(self, frame):
        stack = frame.OperandStack()
        val = stack.PopInt()
        index = stack.PopInt()
        arrRef = stack.PopRef()
        checkNotNil(arrRef)
        ints = arrRef.Ints()
        checkIndex(len(ints), index)
        ints[index] = val


# class LASTORE(base.NoOperandsInstruction):


# class SASTORE(base.NoOperandsInstruction):
