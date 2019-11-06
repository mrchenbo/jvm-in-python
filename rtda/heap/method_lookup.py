def LookupMethodInClass(clazz, name, descriptor):
    c = clazz
    
    while c is not None:
        for method in c.methods:
            if method.name == name and method.descriptor == descriptor:
                return method
        c = c.superClass

    return None

def lookupMethodInInterfaces(ifaces, name, descriptor):
    for iface in ifaces:
        for method in iface.methods:
            if method.name == name and method.descriptor == descriptor:
                return method

    method = lookupMethodInInterfaces(iface.interfaces, name, descriptor)
    if method != None:
        return method

    return None

def lookupInterfaceMethod(iface, name, descriptor):
    for method in iface.methods:
        if method.name == name and method.descriptor == descriptor:
            return method

    return lookupMethodInInterfaces(iface.interfaces, name, descriptor)

