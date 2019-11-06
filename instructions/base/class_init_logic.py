def InitClass(thread, clazz):
    clazz.StartInit()
    scheduleClinit(thread, clazz)
    initSuperClass(thread, clazz)

def scheduleClinit(thread, clazz):
    clinit = clazz.GetClinitMethod()
    if clinit != None:
        # exec <clinit>
        newFrame = thread.NewFrame(clinit)
        thread.PushFrame(newFrame)

def initSuperClass(thread, clazz):
    if not clazz.IsInterface():
        superClass = clazz.SuperClass()
        if superClass != None and not superClass.InitStarted():
            InitClass(thread, superClass)