from instructions import base


class SWAP ( base.NoOperandsInstruction ):
    def Execute(self, frame):
        stack = frame.OperandStack()
        slot1 = stack.PopSlot()
        slot2 = stack.PopSlot()
        stack.PushSlot(slot1)
        stack.PushSlot(slot2)
