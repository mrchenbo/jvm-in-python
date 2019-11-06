from .local_vars import newLocalVars
from .operand_stack import newOperandStack


class Frame:
    def __init__(self, thread, method, localVars, operandStack):
        self.localVars = localVars
        self.operandStack = operandStack
        self.thread = thread
        self.method = method
        self.nextPC = 0

    def LocalVars(self):
        return self.localVars

    def OperandStack(self):
        return self.operandStack

    def NextPC(self):
        return self.nextPC

    def SetNextPC(self, pc):
        self.nextPC = pc

    def Thread(self):
        return self.thread

    def Method(self):
        return self.method

    def RevertNextPC(self):
        self.nextPC = self.thread.pc


def newFrame(thread, method):
    return Frame(thread, method, newLocalVars(method.MaxLocals()), newOperandStack(method.MaxStack()))
