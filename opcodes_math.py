def stop(evm):
    evm.stop_flag = True

def add(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(a+b)
    evm.pc += 1
    evm.gas_dec(3)

def mul(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(a*b)
    evm.pc += 1
    evm.gas_dec(5)

def sub(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(a-b)
    evm.pc += 1
    evm.gas_dec(3)

def div(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(0 if b == 0 else a // b)
    evm.pc += 1
    evm.gas_dec(5)

pos_or_neg = lambda number: -1 if number < 0 else 1

def sdiv(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    sign = pos_or_neg(a*b)
    evm.stack.push(0 if b == 0 else sign * (abs(a) // abs(b)))
    evm.pc += 1
    evm.gas_dec(5)

def mod(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(0 if b == 0 else a % b)
    evm.pc += 1
    evm.gas_dec(5)

def smod(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    sign = -1 if a < 0 else 1 #sign of divided only
    evm.stack.push(0 if b == 0 else sign * (abs(a) % abs(b)))
    evm.pc += 1
    evm.gas_dec(5)

def addmod(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    N = evm.stack.pop()
    sum = a + b
    evm.stack.push(0 if N == 0 else sum % N)
    evm.pc += 1
    evm.gas_dec(8)

def mulmod(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    N = evm.stack.pop()
    product = a * b
    evm.stack.push(0 if N == 0 else product % N)
    evm.pc += 1
    evm.gas_dec(8)

def size_in_bytes(number):
    import math
    if number == 0: return 1
    bits_needed = math.ceil(math.log2(abs(number) + 1))
    return math.ceil(bits_needed / 8)

def exp(evm):
    a, exponent = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(a ** exponent)
    evm.pc += 1
    evm.gas_dec(10 + (50 * size_in_bytes(exponent)))

def signextend(evm):
    # b tells in which ith byte the sign bit(the last bit of the byte) remains
    b, x = evm.stack.pop(), evm.stack.pop() # x is signed number   the sign is determined by byte b
    if b <= 31:
        testbit = b * 8 + 7
        sign_bit = 1 << testbit
        if x & sign_bit:
            result = x | (2**256 - sign_bit)
        else:
            result = x & (sign_bit - 1)
    else:
        result = x
    evm.stack.push(result)
    evm.pc += 1
    evm.gas_dec(5)
