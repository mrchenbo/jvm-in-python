class SymRef:
    def __init__(self):
        self.cp = None
        self.className = None
        self.clazz = None

    def ResolvedClass(self):
        if self.clazz is None:
            self.resolveClassRef()

        return self.clazz

    def resolveClassRef(self):
        d = self.cp.clazz
        c = d.loader.LoadClass(self.className)
        if not c.isAccessibleTo(d):
            raise KeyError("IllegalAccessError")

        self.clazz = c