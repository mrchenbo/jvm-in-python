from .cp_symref import SymRef


class ClassRef(SymRef):
    def __init__(self):
        super().__init__()


def newClassRef(cp, classInfo):
    ref = ClassRef()
    ref.cp = cp
    ref.className = classInfo.Name()
    return ref
