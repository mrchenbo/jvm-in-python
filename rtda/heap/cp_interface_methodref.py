from .cp_memberref import MemberRef
from .method_lookup import *

class InterfaceMethodRef(MemberRef):
    def __init__(self):
        super().__init__()
        self.method = None

    def ResolvedInterfaceMethod(self):
        if self.method == None:
            self.resolveInterfaceMethodRef()

        return self.method

    def resolveInterfaceMethodRef(self):
        d = self.cp.clazz
        c = self.ResolvedClass()
        if not c.IsInterface():
            raise Exception("java.lang.IncompatibleClassChangeError")

        method = lookupInterfaceMethod(c, self.name, self.descriptor)
        if method == None:
            raise Exception("java.lang.NoSuchMethodError")

        if not method.isAccessibleTo(d):
            raise Exception("java.lang.IllegalAccessError")

        self.method = method


def newInterfaceMethodRef(cp, refInfo):
    ref = InterfaceMethodRef()
    ref.cp = cp
    ref.copyMemberRefInfo(refInfo)
    return ref
