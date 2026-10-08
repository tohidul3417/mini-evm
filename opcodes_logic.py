def _and(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(a & b)
    evm.pc += 1
    evm.gas_dec(3)

def _or(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(a  | b)
    evm.pc += 1
    evm.gas_dec(3)

def _xor(evm):
    a, b = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(a ^ b)
    evm.pc += 1
    evm.gas_dec(3)

def _not(evm):
    a = evm.stack.pop()
    evm.stack.push(~a)
    evm.pc += 1
    evm.gas_dec(3)
