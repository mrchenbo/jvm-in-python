class ExceptionHandler:
    def __init__(self, startPc, endPc, handlerPc, catchType):
        self.startPc = startPc
        self.endPc = endPc
        self.handlerPc = handlerPc
        self.catchType = catchType


class ExceptionTable:
    def __init__(self, table):
        self.table = table

    def findExceptionHandler(self, exClass, pc):
        for handler in self.table:
            if pc >= handler.startPc and pc < handler.endPc:
                if handler.catchType == None:
                    return handler  # catch-all

                catchClass = handler.catchType.ResolvedClass()
                if catchClass == exClass or catchClass.IsSuperClassOf(exClass):
                    return handler

        return None


def newExceptionTable(entries, cp):
    table = [None] * len(entries)

    for i, entry in enumerate(entries):
        table[i] = ExceptionHandler(
            entry.StartPc(),
            entry.EndPc(),
            entry.HandlerPc(),
            getCatchType(entry.CatchType(), cp))

    return ExceptionTable(table)


def getCatchType(index, cp):
    if index == 0:
        return None

    return cp.GetConstant(index)
