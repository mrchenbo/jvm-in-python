from ..attribute import readAttributes
from ..attribute.attr_code import CodeAttribute
from ..attribute.attr_constant_value import ConstantValueAttribute


class MemberInfo:
    def __init__(self, cp, accessFlags, nameIndex, descriptorIndex, attributes):
        self.cp = cp
        self.accessFlags = accessFlags
        self.nameIndex = nameIndex
        self.descriptorIndex = descriptorIndex
        self.attributes = attributes

    def Name(self):
        return self.cp.getUtf8(self.nameIndex)

    def Descriptor(self):
        return self.cp.getUtf8(self.descriptorIndex)

    def CodeAttribute(self):
        for attrInfo in self.attributes:
            if isinstance(attrInfo, CodeAttribute):
                return attrInfo

        return None

    def ConstantValueAttribute(self):
        for attrInfo in self.attributes:
            if isinstance(attrInfo, ConstantValueAttribute):
                return attrInfo

        return None

    def AccessFlags(self):
        return self.accessFlags


def readMembers(reader, cp):
    memberCount = reader.readUint16()
    members = []
    for i in range(memberCount):
        members.append(readMember(reader, cp))

    return members


def readMember(reader, cp):
    return MemberInfo(cp, reader.readUint16(), reader.readUint16(), reader.readUint16(), readAttributes(reader, cp))
