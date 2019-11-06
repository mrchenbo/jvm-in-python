import os

class DirEntry:
    def __init__(self, absDir):
        self.absDir = absDir

    def readClass(self, clazz):
        fileName = os.path.join(self.absDir, clazz)
        if not os.path.exists(fileName):
            return None, self, "class file not exist"
        
        with open(fileName, 'rb') as f:
            return f.read(), self, None

    def __str__(self):
        return self.absDir