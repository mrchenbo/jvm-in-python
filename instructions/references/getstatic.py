from instructions import base

class GET_STATIC(base.Index16Instruction):
    def Execute(self, frame):
        cp = frame.Method().Class().ConstantPool()
        fieldRef = cp.GetConstant(self.Index)
        field = fieldRef.ResolvedField()
        clazz = field.Class()

        if not clazz.InitStarted():
            frame.RevertNextPC()
            base.InitClass(frame.Thread(), clazz)
            return

        if not field.IsStatic():
            raise Exception("java.lang.IncompatibleClassChangeError")

        descriptor = field.Descriptor()
        slotId = field.SlotId()
        slots = clazz.StaticVars()
        stack = frame.OperandStack()
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
