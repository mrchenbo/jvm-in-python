from zipfile import ZipFile

class ZipEntry:
    def __init__(self, absPath):
        self.absPath = absPath
    
    def readClass(self, clazz):
        try:
            zf = ZipFile(self.absPath)
        except FileNotFoundError as e:
            return None, self, "%s zip file not exist" % self.absPath

        for file in zf.namelist():
            if file == clazz:
                with zf.open(file, "r") as myfile:
                    return myfile.read(), self, None

        return None, self, "%s class not found" % clazz
    
    def __str__(self):
        return self.absPath