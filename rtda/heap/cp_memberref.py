from .cp_symref import SymRef


class MemberRef(SymRef):
    def __init__(self):
        super().__init__()
        self.name = None
        self.descriptor = None

    def copyMemberRefInfo(self, refInfo):
        self.className = refInfo.ClassName()
        self.name, self.descriptor = refInfo.NameAndDescriptor()

    def Name(self):
	    return self.name

    def Descriptor(self):
	    return self.descriptor
