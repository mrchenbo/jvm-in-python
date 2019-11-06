from instructions import base

class NEW(base.Index16Instruction):
    def Execute(self, frame):
        cp = frame.Method().Class().ConstantPool()
        classRef = cp.GetConstant(self.Index)
        clazz = classRef.ResolvedClass()

        if not clazz.InitStarted():
            frame.RevertNextPC()
            base.InitClass(frame.Thread(), clazz)
            return
        
        if clazz.IsInterface() or clazz.IsAbstract():
            raise Exception("java.lang.InstantiationError")

        ref = clazz.NewObject()
        frame.OperandStack().PushRef(ref)