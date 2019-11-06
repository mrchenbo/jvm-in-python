from .cp_memberref import MemberRef
from .method_lookup import *

class MethodRef(MemberRef):
    def __init__(self):
        super().__init__()
        self.method = None

    def ResolvedMethod(self):
        if self.method == None:
            self.resolveMethodRef()

        return self.method

    def resolveMethodRef(self):
        d = self.cp.clazz
        c = self.ResolvedClass()
        if c.IsInterface():
            raise Exception("java.lang.IncompatibleClassChangeError")

        method = lookupMethod(c, self.name, self.descriptor)
        if method == None:
            raise Exception("java.lang.NoSuchMethodError")

        if not method.isAccessibleTo(d):
            raise Exception("java.lang.IllegalAccessError")

        self.method = method


def newMethodRef(cp, refInfo):
    ref = MethodRef()
    ref.cp = cp
    ref.copyMemberRefInfo(refInfo)
    return ref

def lookupMethod(clazz, name, descriptor):
    method = LookupMethodInClass(clazz, name, descriptor)
    if method == None:
        method = lookupMethodInInterfaces(clazz.interfaces, name, descriptor)

    return method