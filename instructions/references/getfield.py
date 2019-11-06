from instructions import base


class GET_FIELD(base.Index16Instruction):
    def Execute(self, frame):
        cp = frame.Method().Class().ConstantPool()
        fieldRef = cp.GetConstant(self.Index)
        field = fieldRef.ResolvedField()

        if field.IsStatic():
            raise Exception("java.lang.IncompatibleClassChangeError")

        stack = frame.OperandStack()
        ref = stack.PopRef()
        if ref is None:
            raise Exception("java.lang.NullPointerException")

        descriptor = field.Descriptor()
        slotId = field.SlotId()
        slots = ref.Fields()
        flag = descriptor[0]

        if flag in ('Z', 'B', 'C', 'S', 'I'):
            stack.PushInt(slots.GetInt(slotId))
        elif flag == 'F':
            stack.PushFloat(slots.GetFloat(slotId))
        elif flag == 'J':
            stack.PushLong(slots.GetLong(slotId))
        elif flag == 'D':
            stack.PushDouble(slots.GetDouble(slotId))
        elif flag in ('L', '['):
            stack.PushRef(slots.GetRef(slotId))
