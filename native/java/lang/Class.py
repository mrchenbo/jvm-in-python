import native
from rtda import heap


def getPrimitiveClass(frame):
    nameObj = frame.LocalVars().GetRef(0)
    name = heap.GoString(nameObj)
    loader = frame.Method().Class().Loader()
    clazz = loader.LoadClass(name).JClass()
    frame.OperandStack().PushRef(clazz)


def getName0(frame):
    this = frame.LocalVars().GetThis()
    clazz = this.Extra()
    name = clazz.JavaName()
    nameObj = heap.JString(clazz.Loader(), name)
    frame.OperandStack().PushRef(nameObj)


def desiredAssertionStatus0(frame):
    frame.OperandStack().PushBoolean(False)


native.Register("java/lang/Class", "getPrimitiveClass",
                "(Ljava/lang/String;)Ljava/lang/Class;", getPrimitiveClass)
native.Register("java/lang/Class", "getName0",
                "()Ljava/lang/String;", getName0)
native.Register("java/lang/Class", "desiredAssertionStatus0",
                "(Ljava/lang/Class;)Z", desiredAssertionStatus0)
