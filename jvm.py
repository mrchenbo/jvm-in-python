import rtda
from rtda import heap
from instructions import base
from interpreter import interpret
from classpath import ClassPath


class JVM:
    def __init__(self, cmd, classLoader, mainThread):
        self.cmd = cmd
        self.classLoader = classLoader
        self.mainThread = mainThread

    def start(self):
        self.initVM()
        self.execMain()

    def initVM(self):
        vmClass = self.classLoader.LoadClass("sun/misc/VM")
        base.InitClass(self.mainThread, vmClass)
        interpret(self.mainThread, self.cmd.verboseInstFlag)

    def execMain(self):
        clazz = self.cmd.clazz[0]
        className = clazz.replace(".", "/")
        mainClass = self.classLoader.LoadClass(className)
        mainMethod = mainClass.GetMainMethod()
        if mainMethod == None:
            print("Main method not found in class ", clazz)
            return

        argsArr = self.createArgsArray()
        frame = self.mainThread.NewFrame(mainMethod)
        frame.LocalVars().SetRef(0, argsArr)
        self.mainThread.PushFrame(frame)
        interpret(self.mainThread, self.cmd.verboseInstFlag)

    def createArgsArray(self):
        loader = self.classLoader
        args = self.cmd.args
        stringClass = loader.LoadClass("java/lang/String")
        argsArr = stringClass.ArrayClass().NewArray(len(args))
        jArgs = argsArr.Refs()
        for i, arg in enumerate(args):
            jArgs[i] = heap.JString(loader, arg)

        return argsArr


def newJVM(cmd):
    cp = ClassPath(cmd.Xjre, cmd.classpath)
    classLoader = heap.NewClassLoader(cp)
    return JVM(cmd, classLoader, rtda.NewThread())
