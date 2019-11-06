import native


def fillInStackTrace(frame):
    this = frame.LocalVars().GetThis()
    frame.OperandStack().PushRef(this)
    stes = createStackTraceElements(this, frame.Thread())
    this.SetExtra(stes)


native.Register("java/lang/Throwable", "fillInStackTrace",
                "(I)Ljava/lang/Throwable;", fillInStackTrace)


class StackTraceElement:
    def __init__(self, fileName, className, methodName, lineNumber):
        self.fileName = fileName
        self.className = className
        self.methodName = methodName
        self.lineNumber = lineNumber

    def __str__(self):
        return "fileName:{0}, className:{1}, methodName:{2}, lineNumber:{3}".format(self.fileName, self.className, self.methodName, self.lineNumber)


def createStackTraceElements(tObj, thread):
    skip = distanceToObject(tObj.Class()) + 2
    frames = thread.GetFrames()[skip:]
    stes = []
    for frame in frames:
        stes.append(createStackTraceElement(frame))

    return stes


def distanceToObject(clazz):
    distance = 0
    c = clazz.SuperClass()
    while c is not None:
        distance += 1
        c = c.SuperClass()

    return distance


def createStackTraceElement(frame):
    method = frame.Method()
    clazz = method.Class()

    return StackTraceElement(
        clazz.SourceFile(),
        clazz.JavaName(),
        method.Name(),
        method.GetLineNumber(frame.NextPC() - 1),
    )
