from instructions import base


class PUT_STATIC(base.Index16Instruction):
    def Execute(self, frame):
        currentMethod = frame.Method()
        currentClass = currentMethod.Class()
        cp = currentClass.ConstantPool()
        fieldRef = cp.GetConstant(self.Index)
        field = fieldRef.ResolvedField()
        clazz = field.Class()

        if not clazz.InitStarted():
            frame.RevertNextPC()
            base.InitClass(frame.Thread(), clazz)
            return

        if not field.IsStatic():
            raise Exception("java.lang.IncompatibleClassChangeError")

        if field.IsFinal():
            if currentClass != clazz or currentMethod.Name() != "<clinit>":
                raise Exception("java.lang.IllegalAccessError")

        descriptor = field.Descriptor()
        slotId = field.SlotId()
        slots = clazz.StaticVars()
        stack = frame.OperandStack()
        flag = descriptor[0]
        if flag in ('Z', 'B', 'C', 'S', 'I'):
            slots.SetInt(slotId, stack.PopInt())
        elif flag == 'F':
            slots.SetFloat(slotId, stack.PopFloat())
        elif flag == 'J':
            slots.SetLong(slotId, stack.PopLong())
        elif flag == 'D':
            slots.SetDouble(slotId, stack.PopDouble())
        elif flag in ('L', '['):
            slots.SetRef(slotId, stack.PopRef())
