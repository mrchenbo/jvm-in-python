from .class_member import ClassMember


class Field(ClassMember):
    def __init__(self):
        super().__init__()
        self.slotId = None
        self.constValueIndex = 0

    def isLongOrDouble(self):
        return self.descriptor == "J" or self.descriptor == "D"

    def copyAttributes(self, cfField):
        valAttr = cfField.ConstantValueAttribute()
        if valAttr != None:
            self.constValueIndex = valAttr.ConstantValueIndex()

    def SlotId(self):
        return self.slotId

    def ConstValueIndex(self):
        return self.constValueIndex


def newFields(clazz, cfFields):
    fields = [None] * len(cfFields)
    for i, cfField in enumerate(cfFields):
        fields[i] = Field()
        fields[i].clazz = clazz
        fields[i].copyMemberInfo(cfField)
        fields[i].copyAttributes(cfField)

    return fields
