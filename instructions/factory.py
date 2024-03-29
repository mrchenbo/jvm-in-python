from .constants import *
from .stores import *
from .loads import *
from .comparisons import *
from .math import *
from .control import *
from .references import *
from .stack import *
from .control import *
from .reserved import *
from .extended import *
from .conversions import *

def NewInstruction(opcode):
    instructions = {
        0x00: NOP,
        0x01: ACONST_NULL,
        0x02: ICONST_M1,
        0x03: ICONST_0,
        0x04: ICONST_1,
        0x05: ICONST_2,
        0x06: ICONST_3,
        0x07: ICONST_4,
        0x08: ICONST_5,
        0x0b: FCONST_0,
        0x10: BIPUSH,
        0x11: SIPUSH,
        0x12: LDC,
        0x14: LDC2_W,
        0x15: ILOAD,
        0x19: ALOAD,
        0x1a: ILOAD_0,
        0x1b: ILOAD_1,
        0x1c: ILOAD_2,
        0x1d: ILOAD_3,
        0x22: FLOAD_0,
        0x23: FLOAD_1,
        0x24: FLOAD_2,
        0x2a: ALOAD_0,
        0x2b: ALOAD_1,
        0x2c: ALOAD_2,
        0x2d: ALOAD_3,
        0x2e: IALOAD,
        0x30: FALOAD,
        0x32: AALOAD,
        0x34: CALOAD,
        0x36: ISTORE,
        0x3a: ASTORE,
        0x3b: ISTORE_0,
        0x3c: ISTORE_1,
        0x3d: ISTORE_2,
        0x3e: ISTORE_3,
        0x4c: ASTORE_1,
        0x4d: ASTORE_2,
        0x4e: ASTORE_3,
        0x4f: IASTORE,
        0x53: AASTORE,
        0x55: CASTORE,
        0x57: POP,
        0x59: DUP,
        0x5a: DUP_X1,
        0x60: IADD,
        0x61: LADD,
        0x64: ISUB,
        0x68: IMUL,
        0x6a: FMUL,
        0x6c: IDIV,
        0x70: IREM,
        0x78: ISHL,
        0x79: LSHL,
        0x7a: ISHR,
        0x7c: IUSHR,
        0x7e: IAND,
        0x7f: LAND,
        0x84: IINC,
        0x85: I2L,
        0x86: I2F,
        0x8b: F2I,
        0x95: FCMPL,
        0x96: FCMPG,
        0x99: IFEQ,
        0x9a: IFNE,
        0x9c: IFGE,
        0x9d: IFGT,
        0x9e: IFLE,
        0x9f: IF_ICMPEQ,
        0xa0: IF_ICMPNE,
        0xa1: IF_ICMPLT, 
        0xa2: IF_ICMPGE, 
        0xa3: IF_ICMPGT,
        0xa4: IF_ICMPLE,
        0xa6: IF_ACMPNE,
        0xa7: GOTO,
        0xac: IRETURN,
        0xad: LRETURN,
        0xae: FRETURN,
        0xaf: DRETURN,
        0xb0: ARETURN,
        0xb1: RETURN,
        0xb2: GET_STATIC,
        0xb3: PUT_STATIC,
        0xb4: GET_FIELD,
        0xb5: PUT_FIELD,
        0xb6: INVOKE_VIRTUAL,
        0xb7: INVOKE_SPECIAL,
        0xb8: INVOKE_STATIC,
        0xb9: INVOKE_INTERFACE,
        0xbb: NEW,
        0xbc: NEW_ARRAY,
        0xbd: ANEW_ARRAY,
        0xbe: ARRAY_LENGTH,
        0xbf: ATHROW,
        0xc0: CHECK_CAST,
        0xc1: INSTANCE_OF,
        0xc6: IFNULL,
        0xc7: IFNONNULL,  
        0xfe: INVOKE_NATIVE,
    }

    return instructions[opcode]()
