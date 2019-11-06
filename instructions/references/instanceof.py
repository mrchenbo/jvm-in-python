from instructions import base

class INSTANCE_OF(base.Index16Instruction):
    def Execute(self, frame):
        stack = frame.OperandStack()
        ref = stack.PopRef()
        if ref is None: 
            stack.PushInt(0)
            return

        cp = frame.Method().Class().ConstantPool()
        classRef = cp.GetConstant(self.Index)
        clazz = classRef.ResolvedClass()
        if ref.IsInstanceOf(clazz):
            stack.PushInt(1)
        else:
            stack.PushInt(0)

