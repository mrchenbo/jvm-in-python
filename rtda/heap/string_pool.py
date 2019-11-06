from .object import Object, utf16ToString

internedStrings = {}


def JString(loader, pyStr):
    if pyStr in internedStrings:
        return internedStrings[pyStr]

    chars = stringToUtf16(pyStr)
    jChars = Object(loader.LoadClass("[C"), chars)
    jStr = loader.LoadClass("java/lang/String").NewObject()
    jStr.SetRefVar("value", "[C", jChars)
    internedStrings[pyStr] = jStr
    return jStr


def stringToUtf16(s):
    return s


def GoString(jStr):
    charArr = jStr.GetRefVar("value", "[C")
    return utf16ToString(charArr.Chars())


def InternString(jStr):
    goStr = GoString(jStr)
    if goStr in internedStrings:
        return internedStrings[goStr]

    internedStrings[goStr] = jStr
    return jStr
