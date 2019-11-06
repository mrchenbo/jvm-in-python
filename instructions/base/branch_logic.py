def Branch(frame, offset):
    pc = frame.Thread().PC()
    nextPC = pc + offset
    frame.SetNextPC(nextPC)
