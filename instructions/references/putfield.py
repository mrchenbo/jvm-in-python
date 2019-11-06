from instructions import base


class PUT_FIELD(base.Index16Instruction):
    def Execute(self, frame):
        currentMethod = frame.Method()
        currentClass = currentMethod.Class()
        cp = currentClass.ConstantPool()
        fieldRef = cp.GetConstant(self.Index)
        field = fieldRef.ResolvedField()
        clazz = field.Class()

        if field.IsStatic():
            raise Exception("java.lang.IncompatibleClassChangeError")

        if field.IsFinal():
            if currentClass != clazz or currentMethod.Name() != "<init>":
                raise Exception("java.lang.IllegalAccessError")

        descriptor = field.Descriptor()
        slotId = field.SlotId()
        stack = frame.OperandStack()
        flag = descriptor[0]
        if flag in ('Z', 'B', 'C', 'S', 'I'):
            val = stack.PopInt()
            ref = stack.PopRef()
            if ref is None:
                raise Exception("java.lang.NullPointerException")
            ref.Fields().SetInt(slotId, val)
        elif flag == 'F':
            val = stack.PopFloat()
            ref = stack.PopRef()
            if ref is None:
                raise Exception("java.lang.NullPointerException")
            ref.Fields().SetFloat(slotId, val)
        elif flag == 'J':
            val = stack.PopLong()
            ref = stack.PopRef()
            if ref is None:
                raise Exception("java.lang.NullPointerException")
            ref.Fields().SetLong(slotId, val)
        elif flag == 'D':
            val = stack.PopDouble()
            ref = stack.PopRef()
            if ref is None:
                raise Exception("java.lang.NullPointerException")
            ref.Fields().SetDouble(slotId, val)
        elif flag in ('L', '['):
            val = stack.PopRef()
            ref = stack.PopRef()
            if ref is None:
                raise Exception("java.lang.NullPointerException")
            ref.Fields().SetRef(slotId, val)
