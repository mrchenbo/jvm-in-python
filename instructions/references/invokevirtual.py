from instructions import base
from rtda import heap


class INVOKE_VIRTUAL(base.Index16Instruction):
    def Execute(self, frame):
        currentClass = frame.Method().Class()
        cp = currentClass.ConstantPool()
        methodRef = cp.GetConstant(self.Index)
        resolvedMethod = methodRef.ResolvedMethod()
        if resolvedMethod.IsStatic():
            raise Exception("java.lang.IncompatibleClassChangeError")

        ref = frame.OperandStack().GetRefFromTop(resolvedMethod.ArgSlotCount() - 1)
        if ref == None:
            # hack!
            if methodRef.Name() == "println":
                _println(frame.OperandStack(), methodRef.Descriptor())
                return

            raise Exception("java.lang.NullPointerException")

        if resolvedMethod.IsProtected() and resolvedMethod.Class().IsSuperClassOf(currentClass) and \
                resolvedMethod.Class().GetPackageName() != currentClass.GetPackageName() and ref.Class() != currentClass and \
                not ref.Class().IsSubClassOf(currentClass):
            raise Exception("java.lang.IllegalAccessError")

        methodToBeInvoked = heap.LookupMethodInClass(
            ref.Class(), methodRef.Name(), methodRef.Descriptor())
        if methodToBeInvoked == None or methodToBeInvoked.IsAbstract():
            raise Exception("java.lang.AbstractMethodError")

        base.InvokeMethod(frame, methodToBeInvoked)


def _println(stack, descriptor):

    if descriptor == "(Z)V":
        print("{0}".format(stack.PopInt() != 0))
    elif descriptor == "(C)V":
        print("{0}".format(stack.PopInt()))
    elif descriptor == "(B)V":
        print("{0}".format(stack.PopInt()))
    elif descriptor == "(S)V":
        print("{0}".format(stack.PopInt()))
    elif descriptor == "(I)V":
        print("{0}".format(stack.PopInt()))
    elif descriptor == "(F)V":
        print("{0}".format(stack.PopFloat()))
    elif descriptor == "(J)V":
        print("{0}".format(stack.PopLong()))
    elif descriptor == "(D)V":
        print("{0}".format(stack.PopDouble()))
    elif descriptor == "(Ljava/lang/String;)V":
        jStr = stack.PopRef()
        goStr = heap.GoString(jStr)
        print(goStr)
    else:
        raise Exception("println: " + descriptor)

    stack.PopRef()
