import native
from rtda import heap
from instructions import base

def initialize(frame):  # hack: just make VM.savedProps nonempty
    vmClass = frame.Method().Class()
    savedProps = vmClass.GetRefVar("savedProps", "Ljava/util/Properties;")
    key = heap.JString(vmClass.Loader(), "foo")
    val = heap.JString(vmClass.Loader(), "bar")

    frame.OperandStack().PushRef(savedProps)
    frame.OperandStack().PushRef(key)
    frame.OperandStack().PushRef(val)

    propsClass = vmClass.Loader().LoadClass("java/util/Properties")
    setPropMethod = propsClass.GetInstanceMethod("setProperty",
                                                 "(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/Object;")
    base.InvokeMethod(frame, setPropMethod)


native.Register("sun/misc/VM", "initialize", "()V", initialize)
