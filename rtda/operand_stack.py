class OperandStack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.__list = []

    def _push(self, val):
        if len(self.__list) >= self.maxSize:
            raise OverflowError
        self.__list.append(val)

    def _pop(self):
        return self.__list.pop()

    def PushInt(self, val):
        self._push(val)

    def PopInt(self):
        return self._pop()

    def PushFloat(self, val):
        self._push(val)

    def PopFloat(self):
        return self._pop()

    def PushLong(self, val):
        self._push(val)

    def PopLong(self):
        return self._pop()

    def PushDouble(self, val):
        self._push(val)

    def PopDouble(self):
        return self._pop()

    def PushBoolean(self, val):
        self._push(val)

    def PushRef(self, val):
        self._push(val)

    def PopRef(self):
        return self._pop()

    def PushSlot(self, slot):
        self._push(slot)

    def PopSlot(self):
        return self._pop()

    def GetRefFromTop(self, n):
        return self.__list[-1-n]

    def Clear(self):
        self.size = 0
        self.__list = []

    def __str__(self):
        return str(self.__list)


def newOperandStack(maxStack):
    if maxStack > 0:
        return OperandStack(maxStack)

    return None
