class LocalVars:
    def __init__(self, size):
        self.__list = [None] * size

    def _set(self, index, val):
        self.__list[index] = val

    def _get(self, index):
        return self.__list[index]

    def SetInt(self, index, val):
        self._set(index, val)

    def GetInt(self, index):
        return self._get(index)

    def SetFloat(self, index, val):
        self._set(index, val)

    def GetFloat(self, index):
        return self._get(index)

    def SetLong(self, index, val):
        self._set(index, val)

    def GetLong(self, index):
        return self._get(index)

    def SetDouble(self, index, val):
        self._set(index, val)

    def GetDouble(self, index):
        return self._get(index)

    def SetRef(self, index, val):
        self._set(index, val)

    def GetRef(self, index):
        return self._get(index)

    def SetSlot(self, index, slot):
        self._set(index, slot)

    def GetThis(self):
        return self.GetRef(0)

    def __str__(self):
        return str(self.__list)


def newLocalVars(maxLocals):
    if maxLocals > 0:
        return LocalVars(maxLocals)
    return None
