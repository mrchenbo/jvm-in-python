class IINC:
    def FetchOperands(self, reader):
        self.Index = reader.ReadUint8()
        self.Const = reader.ReadInt8()

    def Execute(self, frame):
        localVars = frame.LocalVars()
        val = localVars.GetInt(self.Index)
        val += self.Const
        localVars.SetInt(self.Index, val)
