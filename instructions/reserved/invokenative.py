from instructions import base
import native
import native.java.lang
import native.sum.misc

class INVOKE_NATIVE(base.NoOperandsInstruction):
    def Execute(self, frame):
        method = frame.Method()
        className = method.Class().Name()
        methodName = method.Name()
        methodDescriptor = method.Descriptor()
        nativeMethod = native.FindNativeMethod(className, methodName, methodDescriptor)
        if nativeMethod == None:
            methodInfo = className + "." + methodName + methodDescriptor
            raise Exception("java.lang.UnsatisfiedLinkError: " + methodInfo)

        nativeMethod(frame)