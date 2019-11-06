from .method_descriptor import MethodDescriptor


class MethodDescriptorParser:
    def __init__(self):
	    self.raw = None
	    self.offset = 0
	    self.parsed = None

    def parse(self, descriptor):
        self.raw = descriptor
        self.parsed = MethodDescriptor()
        self.startParams()
        self.parseParamTypes()
        self.endParams()
        self.parseReturnType()
        self.finish()
        return self.parsed

    def startParams(self):
        if self.readUint8() != '(':
            self.causePanic()

    def endParams(self):
        if self.readUint8() != ')':
            self.causePanic()

    def finish(self):
        if self.offset != len(self.raw):
            self.causePanic()

    def causePanic(self):
        raise Exception("BAD descriptor: " + self.raw)

    def readUint8(self):
        b = self.raw[self.offset]
        self.offset += 1
        return b

    def unreadUint8(self):
        self.offset -= 1

    def parseParamTypes(self):
        while True:
            t = self.parseFieldType()
            if t != "":
                self.parsed.addParameterType(t)
            else:
                break
            
    def parseReturnType(self):
        if self.readUint8() == 'V':
            self.parsed.returnType = "V"
            return
        

        self.unreadUint8()
        t = self.parseFieldType()
        if t != "":
            self.parsed.returnType = t
            return
        

        self.causePanic()
    

    def parseFieldType(self):
        f = self.readUint8()
        if f == 'B':
            return "B"
        elif f == 'C':
            return "C"
        elif f == 'D':
            return "D"
        elif f == 'F':
            return "F"
        elif f == 'I':
            return "I"
        elif f == 'J':
            return "J"
        elif f == 'S':
            return "S"
        elif f == 'Z':
            return "Z"
        elif f == 'L':
            return self.parseObjectType()
        elif f == '[':
            return self.parseArrayType()
        else:
            self.unreadUint8()
            return ""
        
    def parseObjectType(self):
        unread = self.raw[self.offset:]
        semicolonIndex = unread.find(';')
        if semicolonIndex == -1:
            self.causePanic()
            return ""
        else:
            objStart = self.offset - 1
            objEnd = self.offset + semicolonIndex + 1
            self.offset = objEnd
            descriptor = self.raw[objStart:objEnd]
            return descriptor
    
    def parseArrayType(self):
        arrStart = self.offset - 1
        self.parseFieldType()
        arrEnd = self.offset
        descriptor = self.raw[arrStart:arrEnd]
        return descriptor
    

def parseMethodDescriptor(descriptor):
    parser = MethodDescriptorParser()
    return parser.parse(descriptor)


