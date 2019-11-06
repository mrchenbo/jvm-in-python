from .access_flags import *


class ClassMember:
    def __init__(self):
        self.accessFlags = None
        self.name = None
        self.descriptor = None
        self.clazz = None

    def copyMemberInfo(self, memberInfo):
        self.accessFlags = memberInfo.AccessFlags()
        self.name = memberInfo.Name()
        self.descriptor = memberInfo.Descriptor()

    def isAccessibleTo(self, d):
        if self.IsPublic():
            return True

        c = self.clazz
        if self.IsProtected():
            return d == c or d.IsSubClassOf(c) or c.getPackageName() == d.getPackageName()

        if not self.IsPrivate():
            return c.getPackageName() == d.getPackageName()

        return d == c

    def IsPublic(self):
        return 0 != self.accessFlags & ACC_PUBLIC

    def IsPrivate(self):
        return 0 != self.accessFlags & ACC_PRIVATE

    def IsProtected(self):
        return 0 != self.accessFlags & ACC_PROTECTED

    def IsStatic(self):
        return 0 != self.accessFlags & ACC_STATIC

    def IsFinal(self):
        return 0 != self.accessFlags & ACC_FINAL

    def IsSynthetic(self):
        return 0 != self.accessFlags & ACC_SYNTHETIC

    def IsAbstract(self):
        return 0 != self.accessFlags & ACC_ABSTRACT

    def IsNative(self):
        return 0 != self.accessFlags & ACC_NATIVE

    def Class(self):
        return self.clazz

    def Descriptor(self):
        return self.descriptor

    def Name(self):
        return self.name
