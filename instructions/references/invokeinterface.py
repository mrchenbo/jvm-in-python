from instructions import base
from rtda import heap


class INVOKE_INTERFACE(base.Instruction):
    def FetchOperands(self, reader):
        self.index = reader.ReadUint16()
        reader.ReadUint8()  # count
        reader.ReadUint8()  # must be 0

    def Execute(self, frame):
        cp = frame.Method().Class().ConstantPool()
        methodRef = cp.GetConstant(self.index)
        resolvedMethod = methodRef.ResolvedInterfaceMethod()
        if resolvedMethod.IsStatic() and resolvedMethod.IsPrivate():
            raise Exception("java.lang.IncompatibleClassChangeError")

        ref = frame.OperandStack().GetRefFromTop(resolvedMethod.ArgSlotCount() - 1)
        if ref == None:
            raise Exception("java.lang.NullPointerException")

        if not ref.Class().IsImplements(methodRef.ResolvedClass()):
            raise Exception("java.lang.IncompatibleClassChangeError")

        methodToBeInvoked = heap.LookupMethodInClass(
            ref.Class(), methodRef.Name(), methodRef.Descriptor())
        if methodToBeInvoked == None or methodToBeInvoked.IsAbstract():
            raise Exception("java.lang.AbstractMethodError")

        if not methodToBeInvoked.IsPublic():
            raise Exception("java.lang.IllegalAccessError")

        base.InvokeMethod(frame, methodToBeInvoked)
