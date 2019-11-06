import native
from rtda import heap

def internl(frame):
    this = frame.LocalVars().GetThis()
    interned = heap.InternString(this)
    frame.OperandStack().PushRef(interned)


native.Register("java/lang/String", "intern", "()Ljava/lang/String;", internl) 
