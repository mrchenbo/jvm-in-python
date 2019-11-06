def checkNotNil(ref):
    if ref == None:
        raise Exception("java.lang.NullPointerException")

def checkIndex(arrLen, index):
    if index < 0 or index >= arrLen:
        raise Exception("ArrayIndexOutOfBoundsException")
