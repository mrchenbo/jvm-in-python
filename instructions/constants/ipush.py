class BIPUSH:
    def FetchOperands(self, reader):
        self.val = reader.ReadInt8()

    def Execute(self, frame):
        frame.OperandStack().PushInt(self.val)


class SIPUSH:
    def FetchOperands(self, reader):
        self.val = reader.ReadInt16()

    def Execute(self, frame):
        frame.OperandStack().PushInt(self.val)
