def lt(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(1 if a < b else 0)
    evm.pc += 1
    evm.gas_dec(3)


#helper function
def unsigned_to_signed(x):
    return x - (1 << 256) if x >= (1 << 255) else x

def slt(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    a, b = unsigned_to_signed(a), unsigned_to_signed(b)
    evm.stack.push(1 if a < b else 0)
    evm.pc += 1
    evm.gas_dec(3)

def gt(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(1 if a > b else 0)
    evm.pc += 1
    evm.gas_dec(3)

def sgt(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    a, b = unsigned_to_signed(a), unsigned_to_signed(b)
    evm.stack.push(1 if a > b else 0)
    evm.pc += 1
    evm.gas_dec(3)

def eq(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(1 if a == b else 0)
    evm.pc += 1
    evm.gas_dec(3)

def iszero(evm):
    a = evm.stack.pop()
    evm.stack.push(1 if a == 0 else 1)
    evm.pc += 1
    evm.gas_dec(3)


