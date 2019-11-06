from instructions import base

class CHECK_CAST(base.Index16Instruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        ref = stack.PopRef()
        stack.PushRef(ref)
        if ref == None:
            return

        cp = frame.Method().Class().ConstantPool()
        classRef = cp.GetConstant(self.Index)
        clazz = classRef.ResolvedClass()
        if not ref.IsInstanceOf(clazz):
            raise Exception("java.lang.ClassCastException")
