import os

from .dir_entry import DirEntry
from .composite_entry import CompositeEntry
from .zip_entry import ZipEntry

pathsep = os.pathsep


def newEntry(path):
    if pathsep in path:
        return newCompositeEntry(path)
    if path.endswith("*"):
        return newWildcardEntry(path)
    if path.endswith(".jar") or path.endswith(".JAR") or path.endswith(".zip") or path.endswith(".ZIP"):
        return newZipEntry(path)
    return newDirEntry(path)


def newDirEntry(path):
    absDir = os.path.abspath(path)
    return DirEntry(path)


def newZipEntry(path):
    absPath = os.path.abspath(path)
    return ZipEntry(absPath)


def newCompositeEntry(pathList):
    compositeEntry = []
    for path in pathList.split(pathsep):
        entry = newEntry(path)
        compositeEntry.append(entry)

    return CompositeEntry(compositeEntry)


def newWildcardEntry(path):
    baseDir = path[:-1]  # remove *

    content = os.listdir(baseDir)
    content = [os.path.join(baseDir, fl) for fl in content]

    jar_files = [fl for fl in content if os.path.isfile(
        fl) and (fl.endswith('.jar') or fl.endswith('.JAR'))]
    
    return newCompositeEntry(pathsep.join([os.path.abspath(fl) for fl in jar_files]))


class ClassPath:
    def __init__(self, jreOptions, cpOption):
        jreDir = self.getJreDir(jreOptions)
        jreLibPath = os.path.join(jreDir, "lib", "*")
        jreExtPath = os.path.join(jreDir, "lib", "ext", "*")
        self.bootClasspath = newWildcardEntry(jreLibPath)
        self.extClasspath = newWildcardEntry(jreExtPath)

        if cpOption is None:
            cpOption = '.'
        self.userClasspath = newEntry(cpOption)

    def getJreDir(self, jreOption):
        if jreOption is not None and os.path.exists(jreOption):
            return jreOption
        
        if os.path.exists('./jre'):
            return './jre'

        jh = os.getenv("JAVA_HOME")
        if jh is not None:
            return os.path.join(jh, 'jre')

        raise FileNotFoundError("jre path not exist")

    def ReadClass(self, clazz):
        className = clazz + ".class"
        data, entry, err = self.bootClasspath.readClass(className)
        if err is None:
            return data, entry, err

        data, entry, err = self.extClasspath.readClass(className)
        if err is None:
            return data, entry, err

        return self.userClasspath.readClass(className)

    def __str__(self):
        return str(self.userClasspath)
