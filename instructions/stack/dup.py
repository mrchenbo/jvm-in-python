from instructions import base


class DUP (base.NoOperandsInstruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        slot = stack.PopSlot()
        stack.PushSlot(slot)
        stack.PushSlot(slot)

# Duplicate the top operand stack value and insert two values down


class DUP_X1(base.NoOperandsInstruction):

    def Execute(self, frame):
        stack = frame.OperandStack()
        slot1 = stack.PopSlot()
        slot2 = stack.PopSlot()
        stack.PushSlot(slot1)
        stack.PushSlot(slot2)
        stack.PushSlot(slot1)


# Duplicate the top operand stack value and insert two or three values down
class DUP_X2(base.NoOperandsInstruction):

    def Execute(self, frame):
        stack = frame.OperandStack()
        slot1 = stack.PopSlot()
        slot2 = stack.PopSlot()
        slot3 = stack.PopSlot()
        stack.PushSlot(slot1)
        stack.PushSlot(slot3)
        stack.PushSlot(slot2)
        stack.PushSlot(slot1)


# Duplicate the top one or two operand stack values
class DUP2(base.NoOperandsInstruction):

    def Execute(self, frame):
        stack = frame.OperandStack()
        slot1 = stack.PopSlot()
        slot2 = stack.PopSlot()
        stack.PushSlot(slot2)
        stack.PushSlot(slot1)
        stack.PushSlot(slot2)
        stack.PushSlot(slot1)


# Duplicate the top one or two operand stack values and insert two or three values down
class DUP2_X1(base.NoOperandsInstruction):

    def Execute(self, frame):
        stack = frame.OperandStack()
        slot1 = stack.PopSlot()
        slot2 = stack.PopSlot()
        slot3 = stack.PopSlot()
        stack.PushSlot(slot2)
        stack.PushSlot(slot1)
        stack.PushSlot(slot3)
        stack.PushSlot(slot2)
        stack.PushSlot(slot1)


# Duplicate the top one or two operand stack values and insert two, three, or four values down
class DUP2_X2(base.NoOperandsInstruction):

    def Execute(self, frame):
        stack = frame.OperandStack()
        slot1 = stack.PopSlot()
        slot2 = stack.PopSlot()
        slot3 = stack.PopSlot()
        slot4 = stack.PopSlot()
        stack.PushSlot(slot2)
        stack.PushSlot(slot1)
        stack.PushSlot(slot4)
        stack.PushSlot(slot3)
        stack.PushSlot(slot2)
        stack.PushSlot(slot1)
