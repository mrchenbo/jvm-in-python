class CompositeEntry:
    def __init__(self, entrys):
        self.entrys = entrys

    def readClass(self, clazz):
        for entry in self.entrys:
            data, fromer, err = entry.readClass(clazz)
            if err is None:
                return  data, fromer, None

        return None, self, "class file not exist"

    def __str__(self):
        return ''.join(self.entrys)