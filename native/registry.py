registry = {}

def Register(className, methodName, methodDescriptor, method):
    key = className + "~" + methodName + "~" + methodDescriptor
    registry[key] = method

def FindNativeMethod(className, methodName, methodDescriptor):
    key = className + "~" + methodName + "~" + methodDescriptor
    if key in registry:
        return registry[key]
    
    if methodDescriptor == "()V" and methodName == "registerNatives":
        return emptyNativeMethod
   
    return None

def emptyNativeMethod(frame):
    pass
