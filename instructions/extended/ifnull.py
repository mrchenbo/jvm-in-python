from instructions import base


class IFNONNULL(base.BranchInstruction):

    def Execute(self, frame):
        ref = frame.OperandStack().PopRef()
        if ref != None:
            base.Branch(frame, self.Offset)


class IFNULL(base.BranchInstruction):

    def Execute(self, frame):
        ref = frame.OperandStack().PopRef()
        if ref == None:
            base.Branch(frame, self.Offset)
