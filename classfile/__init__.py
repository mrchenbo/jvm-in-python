from .class_file import ClassFile
from .class_reader import ClassReader
from .constant import *
 
def Parse(classData):
    cr = ClassReader(classData)
    cf = ClassFile()
    cf.read(cr)
    return cf