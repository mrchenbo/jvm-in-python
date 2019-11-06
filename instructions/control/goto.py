from instructions import base


class GOTO (base.BranchInstruction):
    def Execute(self, frame):
        base.Branch(frame, self.Offset)