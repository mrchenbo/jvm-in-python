from .cp_memberref import MemberRef


class FieldRef(MemberRef):
    def __init__(self):
        super().__init__()
        self.field = None

    def ResolvedField(self):
        if self.field == None:
            self.resolveFieldRef()

        return self.field

    def resolveFieldRef(self):
        d = self.cp.clazz
        c = self.ResolvedClass()
        field = lookupField(c, self.name, self.descriptor)
        if field == None:
            raise KeyError("java.lang.NoSuchFieldError")

        if not field.isAccessibleTo(d):
            raise KeyError("ava.lang.IllegalAccessError")

        self.field = field


def newFieldRef(cp, refInfo):
    ref = FieldRef()
    ref.cp = cp
    ref.copyMemberRefInfo(refInfo)
    return ref


def lookupField(c, name, descriptor):
    for field in c.fields:
        if field.name == name and field.descriptor == descriptor:
            return field

    for iface in c.interfaces:
        field = lookupField(iface, name, descriptor)
        if field != None:
            return field

    if c.superClass != None:
        return lookupField(c.superClass, name, descriptor)

    return None
