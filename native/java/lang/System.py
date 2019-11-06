import native
from rtda import heap


def arraycopy(frame):
    vars = frame.LocalVars()
    src = vars.GetRef(0)
    srcPos = vars.GetInt(1)
    dest = vars.GetRef(2)
    destPos = vars.GetInt(3)
    length = vars.GetInt(4)

    if src == None or dest == None:
        raise Exception("java.lang.NullPointerException")

    if not checkArrayCopy(src, dest):
        raise Exception("java.lang.ArrayStoreException")

    if srcPos < 0 or destPos < 0 or length < 0 or \
            srcPos+length > src.ArrayLength() or \
            destPos+length > dest.ArrayLength():
        raise Exception("java.lang.IndexOutOfBoundsException")

    heap.ArrayCopy(src, dest, srcPos, destPos, length)


def checkArrayCopy(src, dest):
    srcClass = src.Class()
    destClass = dest.Class()
    if not srcClass.IsArray() or not destClass.IsArray():
        return False

    if srcClass.ComponentClass().IsPrimitive() or \
            destClass.ComponentClass().IsPrimitive():
        return srcClass == destClass

    return True


native.Register("java/lang/System", "arraycopy",
                "(Ljava/lang/Object;ILjava/lang/Object;II)V", arraycopy)
