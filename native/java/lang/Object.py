import native


def getClass(frame):
    this = frame.LocalVars().GetThis()
    clazz = this.Class().JClass()
    frame.OperandStack().PushRef(clazz)


def hashCode(frame):
    this = frame.LocalVars().GetThis()
    hashv = hash(this)
    frame.OperandStack().PushInt(hashv)


def clone(frame):
    this = frame.LocalVars().GetThis()

    cloneable = this.Class().Loader().LoadClass("java/lang/Cloneable")
    if not this.Class().IsImplements(cloneable):
        raise Exception("java.lang.CloneNotSupportedException")

    frame.OperandStack().PushRef(this.Clone())


jlObject = "java/lang/Object"

native.Register(jlObject, "getClass",
                "()Ljava/lang/Class;", getClass)

native.Register(jlObject, "hashCode", "()I", hashCode)
native.Register(jlObject, "clone", "()Ljava/lang/Object;", clone)


