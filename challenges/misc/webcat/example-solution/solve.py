# Note: This is a stripped down version from the original source code of webcat.
#       The same models were used to also generate random code on the server.
#       As a result, the code looks a lot more verbose than is necessary.

from pwn import *
from io import BytesIO
import struct

REG_EAX = 0
REG_ECX = 1
REG_EDX = 2
REG_EBX = 3

REGS = [REG_EAX, REG_EBX, REG_ECX, REG_EDX]
REG_NAMES = {
    REG_EAX: "eax",
    REG_EBX: "ebx",
    REG_ECX: "ecx",
    REG_EDX: "edx",
}

class EvalContext:
    """
    Evaluation context, containing current state of registers and stack.
    """

    def __init__(self):
        self.registers = dict()
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()



class Instruction:
    """
    Stripped down version of the instruction model.
    """

    def eval(self, ctx: EvalContext):
        pass


class MovRegImm(Instruction):

    def __init__(self, reg, imm):
        self.imm = imm
        self.reg = reg


    def eval(self, ctx: EvalContext):
        ctx.registers[self.reg] = self.imm


    def __repr__(self):
        return f"mov {REG_NAMES[self.reg]}, {hex(self.imm)}"


class AddRegImm(Instruction):

    def __init__(self, reg, imm):
        self.imm = imm
        self.reg = reg


    def eval(self, ctx: EvalContext):
        ctx.registers[self.reg] = (ctx.registers[self.reg] + self.imm) & 0xFFFFFFFF


    def __repr__(self):
        return f"add {REG_NAMES[self.reg]}, {hex(self.imm)}"


class AndRegImm(Instruction):

    def __init__(self, reg, imm):
        self.imm = imm
        self.reg = reg


    def eval(self, ctx: EvalContext):
        ctx.registers[self.reg] = (ctx.registers[self.reg] & self.imm)


    def __repr__(self):
        return f"and {REG_NAMES[self.reg]}, {hex(self.imm)}"


class OrRegImm(Instruction):

    def __init__(self, reg, imm):
        self.imm = imm
        self.reg = reg


    def eval(self, ctx: EvalContext):
        ctx.registers[self.reg] = (ctx.registers[self.reg] | self.imm)


    def __repr__(self):
        return f"or {REG_NAMES[self.reg]}, {hex(self.imm)}"


class XorRegImm(Instruction):

    def __init__(self, reg, imm):
        self.imm = imm
        self.reg = reg


    def eval(self, ctx: EvalContext):
        ctx.registers[self.reg] = (ctx.registers[self.reg] ^ self.imm)


    def __repr__(self):
        return f"xor {REG_NAMES[self.reg]}, {hex(self.imm)}"


class ShlRegImm(Instruction):

    def __init__(self, reg, imm):
        self.imm = imm
        self.reg = reg


    def eval(self, ctx: EvalContext):
        ctx.registers[self.reg] = (ctx.registers[self.reg] << self.imm) & 0xFFFFFFFF


    def __repr__(self):
        return f"shl {REG_NAMES[self.reg]}, {hex(self.imm)}"


class ShrRegImm(Instruction):

    def __init__(self, reg, imm):
        self.imm = imm
        self.reg = reg


    def eval(self, ctx: EvalContext):
        ctx.registers[self.reg] = (ctx.registers[self.reg] >> self.imm) & 0xFFFFFFFF


    def __repr__(self):
        return f"shr {REG_NAMES[self.reg]}, {hex(self.imm)}"


class BinReader:
    """
    A simple binary reader implementation.
    """
    def __init__(self,data):
        self.data = data
        self.pc = 0

    def read_byte(self):
        self.pc += 1
        return self.data[self.pc - 1]

    def read_uint32(self):
        self.pc += 4
        return struct.unpack_from("<I", self.data, self.pc - 4)[0]


def disassemble(code):
    """
    Implements a minimal x86 disassembler for the incoming bytes.
    """

    reader = BinReader(code)
    result = []

    while reader.pc < len(code):
        op = reader.read_byte()
        if op == 0xb8:
            result.append(MovRegImm(REG_EAX, reader.read_uint32()))
        elif op == 0x05:
            result.append(AddRegImm(REG_EAX, reader.read_uint32()))
        elif op == 0x25:
            result.append(AndRegImm(REG_EAX, reader.read_uint32()))
        elif op == 0x0d:
            result.append(OrRegImm(REG_EAX, reader.read_uint32()))
        elif op == 0x35:
            result.append(XorRegImm(REG_EAX, reader.read_uint32()))
        elif op == 0x39:
            # cmp, = last instruction. we dont need it.
            break
        elif op == 0xc1:
            op = reader.read_byte()
            if op == 0xe0:
                result.append(ShlRegImm(REG_EAX, reader.read_byte()))
            elif op == 0xe8:
                result.append(ShrRegImm(REG_EAX, reader.read_byte()))

    return result 


p = remote("smoothie.rtn-team.cc", 80)
p.send("hello")

needle = b"Web cat says: "

while True:
    data = p.recvline()
    print(data.decode("utf-8"), end='')
    if b"RTN" in data:
        break
    if needle not in data: 
        continue

    start_idx = data.index(needle)
    end_idx = data.index(b"\n", start_idx)
    hex_data = data[start_idx+len(needle):end_idx].decode("utf-8")

    instructions = disassemble(bytes.fromhex(hex_data))
    ctx = EvalContext()
    for instr in instructions:
        instr.eval(ctx)
    
    p.send(hex(ctx.registers[REG_EAX]) + "\n")

p.close()

