from instructions import base

class ANEW_ARRAY(base.Index16Instruction):
    def Execute(self, frame):
        cp = frame.Method().Class().ConstantPool()
        classRef = cp.GetConstant(self.Index)
        componentClass = classRef.ResolvedClass()
        stack = frame.OperandStack()
        count = stack.PopInt()
        if count < 0:
            raise Exception("java.lang.NegativeArraySizeException")
        
        arrClass = componentClass.ArrayClass()
        arr = arrClass.NewArray(count)
        stack.PushRef(arr)