from instructions import base


class MULTI_ANEW_ARRAY(base.Instruction):
    def __init__(self):
        self.index = 0
        self.dimensions = 0

    def FetchOperands(self, reader):
        self.index = reader.ReadUint16()
        self.dimensions = reader.ReadUint8()

    def Execute(self, frame):
        cp = frame.Method().Class().ConstantPool()
        classRef = cp.GetConstant(self.index)
        arrClass = classRef.ResolvedClass()
        stack = frame.OperandStack()
        counts = popAndCheckCounts(stack, self.dimensions)
        arr = newMultiDimensionalArray(counts, arrClass)
        stack.PushRef(arr)

def popAndCheckCounts(stack, dimensions):
    counts = [None] * dimensions
    i = dimensions - 1
    while i >= 0:
        counts[i] = stack.PopInt()
        if counts[i] < 0:
            raise Exception("java.lang.NegativeArraySizeException")
        i -= 1

    return counts

def newMultiDimensionalArray(counts, arrClass):
    count = counts[0]
    arr = arrClass.NewArray(count)
    if len(counts) > 1:
        refs = arr.Refs()
        for i in range(len(refs)):
            refs[i] = newMultiDimensionalArray (counts[1:], arrClass.ComponentClass())

    return arr