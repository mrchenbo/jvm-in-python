from instructions import base
from rtda import heap


class INVOKE_SPECIAL(base.Index16Instruction):
    def Execute(self, frame):
        currentClass = frame.Method().Class()
        cp = currentClass.ConstantPool()
        methodRef = cp.GetConstant(self.Index)
        resolvedClass = methodRef.ResolvedClass()
        resolvedMethod = methodRef.ResolvedMethod()

        if resolvedMethod.Name() == "<init>" and resolvedMethod.Class() != resolvedClass:
            raise Exception("java.lang.NoSuchMethodError")

        if resolvedMethod.IsStatic():
            raise Exception("java.lang.IncompatibleClassChangeError")

        ref = frame.OperandStack().GetRefFromTop(resolvedMethod.ArgSlotCount()-1)
        if ref == None:
            raise Exception("java.lang.NullPointerException")

        if resolvedMethod.IsProtected() and resolvedMethod.Class().IsSuperClassOf(currentClass) \
            and resolvedMethod.Class().GetPackageName() != currentClass.GetPackageName() \
            and ref.Class() != currentClass and not ref.Class().IsSubClassOf(currentClass):
            raise Exception("java.lang.IllegalAccessError")

        methodToBeInvoked = resolvedMethod
        if currentClass.IsSuper() and resolvedClass.IsSuperClassOf(currentClass) and resolvedMethod.Name() != "<init>":
            methodToBeInvoked = heap.LookupMethodInClass(currentClass.SuperClass(),
                methodRef.Name(), methodRef.Descriptor())

        if methodToBeInvoked == None or methodToBeInvoked.IsAbstract():
            raise Exception("java.lang.AbstractMethodError")

        base.InvokeMethod(frame, methodToBeInvoked)
