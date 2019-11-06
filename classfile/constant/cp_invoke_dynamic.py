

'''
CONSTANT_MethodHandle_info {
    u1 tag;
    u1 reference_kind;
    u2 reference_index;
}
'''


class ConstantMethodHandleInfo:
    def __init__(self):
        self.referenceKind = None
        self.referenceIndex = None

    def readInfo(self, reader):
        self.referenceKind = reader.readUint8()
        self.referenceIndex = reader.readUint16()


# /*
# CONSTANT_MethodType_info {
#     u1 tag;
#     u2 descriptor_index;
# }
# */
class ConstantMethodTypeInfo:
    def __init__(self):
        self.descriptorIndex = None

    def readInfo(self, reader):
        self.descriptorIndex = reader.readUint16()


# /*
# CONSTANT_InvokeDynamic_info {
#     u1 tag;
#     u2 bootstrap_method_attr_index;
#     u2 name_and_class_index;
# }
# */
class ConstantInvokeDynamicInfo:
    def __init__(self):
        self.bootstrapMethodAttrIndex = None
        self.nameAndTypeIndex = None

    def readInfo(self, reader):
        self.bootstrapMethodAttrIndex = reader.readUint16()
        self.nameAndTypeIndex = reader.readUint16()
