from .slots import newSlots


class Object:
    def __init__(self, clazz, data):
        self.clazz = clazz
        self.data = data
        self.extra = None

    def IsInstanceOf(self, clazz):
        return clazz.IsAssignableFrom(self.clazz)

    def Fields(self):
        return self.data

    def Class(self):
        return self.clazz

    def Bytes(self):
        return self.data

    def Shorts(self):
        return self.data

    def Ints(self):
        return self.data

    def Longs(self):
        return self.data

    def Chars(self):
        return self.data

    def Floats(self):
        return self.data

    def Doubles(self):
        return self.data

    def Refs(self):
        return self.data

    def ArrayLength(self):
        return len(self.data)

    def SetRefVar(self, name, descriptor, ref):
        field = self.clazz.getField(name, descriptor, False)
        slots = self.data
        slots.SetRef(field.slotId, ref)

    def GoString(self, jStr):
        charArr = jStr.GetRefVar("value", "[C")
        return utf16ToString(charArr.Chars())

    def GetRefVar(self, name, descriptor):
        field = self.clazz.getField(name, descriptor, False)
        slots = self.data
        return slots.GetRef(field.slotId)

    def Extra(self):
        return self.extra

    def SetExtra(self, extra):
        self.extra = extra

    def Clone(self):
        return Object(self.clazz, self.cloneData())

    def cloneData(self):
        slots = newSlots(len(self.data))
        for i in range(len(self.data)):
            slots._set(i, self.data._get(i))

        return slots


def newObject(clazz):
    return Object(clazz, newSlots(clazz.instanceSlotCount))


def utf16ToString(s):
    return ''.join([x if isinstance(x, str) else chr(x) for x in s])
