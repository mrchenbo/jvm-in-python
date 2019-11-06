from instructions import base


class RETURN(base.NoOperandsInstruction):  # Return void from method
    def Execute(self, frame):
        frame.Thread().PopFrame()


class ARETURN(base.NoOperandsInstruction):  # Return reference from method
    def Execute(self, frame):
        thread = frame.Thread()
        currentFrame = thread.PopFrame()
        invokerFrame = thread.TopFrame()
        ref = currentFrame.OperandStack().PopRef()
        invokerFrame.OperandStack().PushRef(ref)


class DRETURN(base.NoOperandsInstruction):  # Return double from method
    def Execute(self, frame):
        thread = frame.Thread()
        currentFrame = thread.PopFrame()
        invokerFrame = thread.TopFrame()
        val = currentFrame.OperandStack().PopDouble()
        invokerFrame.OperandStack().PushDouble(val)


class FRETURN(base.NoOperandsInstruction):  # Return float from method
    def Execute(self, frame):
        thread = frame.Thread()
        currentFrame = thread.PopFrame()
        invokerFrame = thread.TopFrame()
        val = currentFrame.OperandStack().PopFloat()
        invokerFrame.OperandStack().PushFloat(val)


class IRETURN(base.NoOperandsInstruction):  # Return int from method
    def Execute(self, frame):
        thread = frame.Thread()
        currentFrame = thread.PopFrame()
        invokerFrame = thread.TopFrame()
        retVal = currentFrame.OperandStack().PopInt()
        invokerFrame.OperandStack().PushInt(retVal)


class LRETURN(base.NoOperandsInstruction):  # Return long from method
    def Execute(self, frame):
        thread = frame.Thread()
        currentFrame = thread.PopFrame()
        invokerFrame = thread.TopFrame()
        val = currentFrame.OperandStack().PopLong()
        invokerFrame.OperandStack().PushLong(val)
