from instructions import base

class INVOKE_STATIC(base.Index16Instruction):
    def Execute(self, frame):
        cp = frame.Method().Class().ConstantPool()
        methodRef = cp.GetConstant(self.Index)
        resolvedMethod = methodRef.ResolvedMethod()

        clazz = resolvedMethod.Class()
        if not clazz.InitStarted():
            frame.RevertNextPC()
            base.InitClass(frame.Thread(), clazz)
            return
            
        if not resolvedMethod.IsStatic():
            raise Exception("java.lang.IncompatibleClassChangeError")

        base.InvokeMethod(frame, resolvedMethod)