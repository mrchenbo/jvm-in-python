import instructions
from instructions import base
import rtda
from rtda import heap


def interpret(thread, logInst):
    try:
        loop(thread, logInst)
    except Exception as e:
        catchErr(thread)
        raise e


def loop(thread, logInst):
    reader = base.BytecodeReader()
    while True:
        frame = thread.CurrentFrame()
        pc = frame.NextPC()
        thread.SetPC(pc)

        reader.Reset(frame.Method().Code(), pc)
        opcode = reader.ReadUint8()
        try:
            inst = instructions.NewInstruction(opcode)
        except KeyError as e:
            print('%#x' % opcode)
            raise e

        inst.FetchOperands(reader)
        frame.SetNextPC(reader.PC())
        # execute
        if logInst:
            logInstruction(frame, inst)

        inst.Execute(frame)
        if thread.IsStackEmpty():
            break


def logInstruction(frame, inst):
    method = frame.Method()
    className = method.Class().Name()
    methodName = method.Name()
    pc = frame.Thread().PC()
    print("{0}.{1} pc:{2} inst:{3} local:{4} stack:{5}".format(
        className, methodName, pc, inst, frame.LocalVars(), frame.OperandStack()))


def catchErr(thread):
    while not thread.IsStackEmpty():
        frame = thread.PopFrame()
        method = frame.Method()
        className = method.Class().Name()
        print(">> pc:{0} {1}.{2}{3} local:{4} stack:{5}".format(frame.NextPC(),
                                                                className, method.Name(), method.Descriptor(), frame.LocalVars(), frame.OperandStack()))
