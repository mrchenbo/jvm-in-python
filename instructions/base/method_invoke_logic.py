def InvokeMethod(invokerFrame, method):
    thread = invokerFrame.Thread()
    newFrame = thread.NewFrame(method)
    thread.PushFrame(newFrame)
    argSlotSlot = method.ArgSlotCount()
    
    if argSlotSlot > 0:
        i = argSlotSlot - 1
        while i>=0:
            slot = invokerFrame.OperandStack().PopSlot()
            newFrame.LocalVars().SetSlot(i, slot)
            i -= 1
