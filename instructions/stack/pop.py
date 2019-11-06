from instructions import base 

class POP ( base.NoOperandsInstruction ):
    def Execute(self, frame):
        stack = frame.OperandStack()
        stack.PopSlot()

class POP2 ( base.NoOperandsInstruction ):
    def Execute(self, frame):
        stack = frame.OperandStack()
        stack.PopSlot()
        stack.PopSlot()

