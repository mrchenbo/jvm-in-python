def getArrayClassName(className):
    return "[" + toDescriptor(className)

primitiveTypes = {
        "void": "V",
        "boolean": "Z",
        "byte": "B",
        "short": "S",
        "int": "I",
        "long": "J",
        "char": "C",
        "float": "F",
        "double": "D",
    }


def toDescriptor(className):

    if className[0] == '[':
        return className

    if className in primitiveTypes:
        return primitiveTypes[className]

    return "L" + className + ";"


def getComponentClassName(className):
    if className[0] == '[':
        componentTypeDescriptor = className[1:]
        return toClassName(componentTypeDescriptor)

    raise Exception("Not array: " + className)


def toClassName(descriptor):
    if descriptor[0] == '[':
        return descriptor

    if descriptor[0] == 'L':
        return descriptor[1: -1]

    for className, d in primitiveTypes.items():
        if d == descriptor:
            return className

    raise Exception("Invalid descriptor: " + descriptor)

