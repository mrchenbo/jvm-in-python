from instructions import base


AT_BOOLEAN = 4
AT_CHAR = 5
AT_FLOAT = 6
AT_DOUBLE = 7
AT_BYTE = 8
AT_SHORT = 9
AT_INT = 10
AT_LONG = 11


class NEW_ARRAY(base.Instruction):
    def FetchOperands(self, reader):
        self.atype = reader.ReadUint8()

    def Execute(self, frame):
        stack = frame.OperandStack()
        count = stack.PopInt()
        if count < 0:
            raise Exception("java.lang.NegativeArraySizeException")

        classLoader = frame.Method().Class().Loader()
        arrClass = getPrimitiveArrayClass(classLoader, self.atype)
        arr = arrClass.NewArray(count)
        stack.PushRef(arr)


def getPrimitiveArrayClass(loader, atype):
    if atype == AT_BOOLEAN:
        return loader.LoadClass("[Z")
    if atype == AT_BYTE:
        return loader.LoadClass("[B")
    if atype == AT_CHAR:
        return loader.LoadClass("[C")
    if atype == AT_SHORT:
        return loader.LoadClass("[S")
    if atype == AT_INT:
        return loader.LoadClass("[I")
    if atype == AT_LONG:
        return loader.LoadClass("[J")
    if atype == AT_FLOAT:
        return loader.LoadClass("[F")
    if atype == AT_DOUBLE:
        return loader.LoadClass("[D")
    raise Exception("Invalid atype!")
