from instructions import base
from rtda import heap


class ATHROW(base.NoOperandsInstruction):
    def Execute(self, frame):
        ex = frame.OperandStack().PopRef()
        if ex == None:
            raise Exception("java.lang.NullPointerException")

        thread = frame.Thread()
        if not findAndGotoExceptionHandler(thread, ex):
            handleUncaughtException(thread, ex)


def findAndGotoExceptionHandler(thread, ex):
    while True:
        frame = thread.CurrentFrame()
        pc = frame.NextPC() - 1
        handlerPC = frame.Method().FindExceptionHandler(ex.Class(), pc)
        if handlerPC > 0:
            stack = frame.OperandStack()
            stack.Clear()
            stack.PushRef(ex)
            frame.SetNextPC(handlerPC)
            return True

        thread.PopFrame()
        if thread.IsStackEmpty():
            break

    return False


def handleUncaughtException(thread, ex):
    thread.ClearStack()
    jMsg = ex.GetRefVar("detailMessage", "Ljava/lang/String;")
    goMsg = heap.GoString(jMsg)
    print(ex.Class().JavaName() + ": " + goMsg)

    stes = ex.Extra()
    for ste in stes:
        print("\tat", ste)


