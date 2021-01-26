from z3 import *

expected = bytes.fromhex("62754e771f610f2c0825393b01656555135a6b340346")
inputs = [BitVec(f"inputs{i}", 32) for i in range(22)]

s = Solver()

# Pasted XOR equations.
s.add(expected[0] == inputs[0] ^ inputs[6] ^ inputs[0xc] ^ inputs[0x11])
s.add(expected[1] == inputs[0x12] ^ inputs[1] ^ inputs[4] ^ inputs[5] ^ inputs[0xb] ^ inputs[0xc] ^ inputs[0xf])
s.add(expected[2] == inputs[0x15] ^ inputs[3] ^ inputs[6] ^ inputs[8] ^ inputs[10] ^ inputs[0xb] ^ inputs[0xc] ^ inputs[0xd] ^ inputs[0xf] ^ inputs[0x10] ^ inputs[0x11] ^ inputs[0x12] ^ inputs[0x13])
s.add(expected[3] == inputs[0x12] ^ inputs[0] ^ inputs[5] ^ inputs[0xc] ^ inputs[0xe] ^ inputs[0xf] ^ inputs[0x11])
s.add(expected[4] == inputs[0x15] ^ inputs[0] ^ inputs[3] ^ inputs[5] ^ inputs[6] ^ inputs[8] ^ inputs[0xb] ^ inputs[0xd] ^ inputs[0xe] ^ inputs[0xf] ^ inputs[0x10] ^ inputs[0x13])
s.add(expected[5] == inputs[0x15] ^ inputs[0] ^ inputs[1] ^ inputs[2] ^ inputs[4] ^ inputs[6] ^ inputs[7] ^ inputs[8] ^ inputs[0xb] ^ inputs[0xc] ^ inputs[0xe] ^ inputs[0xf] ^ inputs[0x14])
s.add(expected[6] == inputs[0x15] ^ inputs[0] ^ inputs[1] ^ inputs[2] ^ inputs[4] ^ inputs[6] ^ inputs[7] ^ inputs[8] ^ inputs[0xb] ^ inputs[0xc] ^ inputs[0xd] ^ inputs[0xe] ^ inputs[0xf] ^ inputs[0x14])
s.add(expected[7] == inputs[0x15] ^ inputs[4] ^ inputs[5] ^ inputs[8] ^ inputs[10] ^ inputs[0xb] ^ inputs[0xe] ^ inputs[0x11])
s.add(expected[8] == inputs[0x15] ^ inputs[0] ^ inputs[3] ^ inputs[4] ^ inputs[5] ^ inputs[6] ^ inputs[8] ^ inputs[0xb] ^ inputs[0xd] ^ inputs[0xe] ^ inputs[0xf] ^ inputs[0x10] ^ inputs[0x12] ^ inputs[0x13])
s.add(expected[9] == inputs[0x11] ^ inputs[1] ^ inputs[5] ^ inputs[9] ^ inputs[0xc])
s.add(expected[10] == inputs[0x15] ^ inputs[0] ^ inputs[1] ^ inputs[2] ^ inputs[3] ^ inputs[4] ^ inputs[5] ^ inputs[6] ^ inputs[7] ^ inputs[0xb] ^ inputs[0xe] ^ inputs[0x10] ^ inputs[0x12])
s.add(expected[0xb] == inputs[0x15] ^ inputs[0] ^ inputs[3] ^ inputs[4] ^ inputs[9] ^ inputs[10] ^ inputs[0xb] ^ inputs[0xc] ^ inputs[0xd] ^ inputs[0xe] ^ inputs[0x10] ^ inputs[0x11] ^ inputs[0x12] ^ inputs[0x13])
s.add(expected[0xc] == inputs[0x12] ^ inputs[0] ^ inputs[7] ^ inputs[9] ^ inputs[10] ^ inputs[0xb] ^ inputs[0xc] ^ inputs[0xd] ^ inputs[0xe] ^ inputs[0xf] ^ inputs[0x10] ^ inputs[0x11])
s.add(expected[0xd] == inputs[0x14] ^ inputs[0] ^ inputs[2] ^ inputs[4] ^ inputs[5] ^ inputs[8] ^ inputs[9] ^ inputs[0xc] ^ inputs[0xe] ^ inputs[0xf] ^ inputs[0x10])
s.add(expected[0xe] == inputs[8] ^ inputs[0])
s.add(expected[0xf] == inputs[0x15] ^ inputs[7] ^ inputs[8] ^ inputs[0xb] ^ inputs[0xd] ^ inputs[0xe] ^ inputs[0x10] ^ inputs[0x12])
s.add(expected[0x10] == inputs[0x15] ^ inputs[0] ^ inputs[5] ^ inputs[0xc] ^ inputs[0xe] ^ inputs[0xf] ^ inputs[0x11] ^ inputs[0x12])
s.add(expected[0x11] == inputs[0x10] ^ inputs[4] ^ inputs[8] ^ inputs[10] ^ inputs[0xc] ^ inputs[0xd] ^ inputs[0xe])
s.add(expected[0x12] == inputs[0x15] ^ inputs[0] ^ inputs[1] ^ inputs[5] ^ inputs[6] ^ inputs[7] ^ inputs[8] ^ inputs[9] ^ inputs[0xb] ^ inputs[0xd] ^ inputs[0xe] ^ inputs[0x10])
s.add(expected[0x13] == inputs[0x10] ^ inputs[0] ^ inputs[1] ^ inputs[3] ^ inputs[4] ^ inputs[5] ^ inputs[7] ^ inputs[8] ^ inputs[9] ^ inputs[0xb] ^ inputs[0xf])
s.add(expected[0x14] == inputs[0x14] ^ inputs[1] ^ inputs[2] ^ inputs[4] ^ inputs[6] ^ inputs[7] ^ inputs[8] ^ inputs[9] ^ inputs[10] ^ inputs[0xb] ^ inputs[0xc] ^ inputs[0xe])
s.add(expected[0x15] == inputs[0x15] ^ inputs[0] ^ inputs[2] ^ inputs[5] ^ inputs[7] ^ inputs[8] ^ inputs[9] ^ inputs[10] ^ inputs[0xb] ^ inputs[0xd] ^ inputs[0xe] ^ inputs[0xf] ^ inputs[0x12] ^ inputs[0x14])
        

# Compute result.
result = s.check()
print(result)

if result == sat:
    m = s.model()
    solution = bytearray()
    for i in range(len(inputs)):
        x = m[inputs[i]]
        solution.append(x.as_long())     
    print(solution.decode())

