from .jvm_stack import newStack
from .frame import newFrame


def NewThread():
    return Thread(newStack(1024))


class Thread:
    def __init__(self, stack):
        self.pc = None
        self.stack = stack

    def PushFrame(self, frame):
        self.stack.push(frame)

    def PopFrame(self):
        return self.stack.pop()

    def CurrentFrame(self):
        return self.stack.top()

    def TopFrame(self):
        return self.CurrentFrame()

    def NewFrame(self, method):
        return newFrame(self, method)

    def SetPC(self, pc):
        self.pc = pc

    def PC(self):
        return self.pc

    def IsStackEmpty(self):
        return self.stack.is_empty()

    def ClearStack(self):
        self.stack.clear()

    def GetFrames(self):
        return self.stack.getFrames()
