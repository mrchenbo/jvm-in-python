from .attr_code import *
from .attr_constant_value import *
from .attr_exceptions import *
from .attr_line_number_table import *
from .attr_markers import *
from .attr_source_file import *
from .attr_unparsed import *


def readAttributes(reader, cp):
    attributesCount = reader.readUint16()
    attributes = []
    for i in range(attributesCount):
        attributes.append(readAttribute(reader, cp))
    return attributes

def readAttribute(reader, cp):
    attrNameIndex = reader.readUint16()
    attrName = cp.getUtf8(attrNameIndex)
    attrLen = reader.readUint32()
    attrInfo = newAttributeInfo(attrName, attrLen, cp)
    attrInfo.readInfo(reader)
    return attrInfo

def newAttributeInfo(attrName, attrLen, cp):
    if attrName == "Code":
        return CodeAttribute(cp)
    elif attrName == "ConstantValue":
        return ConstantValueAttribute()
    elif attrName == "Deprecated":
        return DeprecatedAttribute()
    elif attrName == "Exceptions":
        return ExceptionsAttribute()
    elif attrName == "LineNumberTable":
        return LineNumberTableAttribute()
    elif attrName == "LocalVariableTable":
        return LocalVariableTableAttribute()
    elif attrName == "SourceFile":
        return SourceFileAttribute(cp)
    elif attrName == "Synthetic":
        return SyntheticAttribute()
    else:
        return UnparsedAttribute(attrName, attrLen, None)
