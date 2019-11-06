'''
将局部变量表与类实例变量分开定义，因为实例变量有默认初始化值
'''
from ..local_vars import newLocalVars


class Slots:
    def __init__(self, size):
        self.__list = [None] * size

    def _set(self, index, val):
        self.__list[index] = val

    def _get(self, index):
        return self.__list[index]

    def SetInt(self, index, val):
        self._set(index, val)

    def GetInt(self, index):
        res = self._get(index)
        if res is None:
            res = 0
        return res

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

    def __len__(self):
        return len(self.__list)
        
    def __str__(self):
        return str(self.__list)


def newSlots(maxLocals):
    if maxLocals > 0:
        return Slots(maxLocals)
    return None
