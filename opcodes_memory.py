def mload(evm):
    offset = evm.stack.pop()
    value = evm.memory.load(offset)
    evm.stack.push(value)
    pc += 1

def mstore(evm):
    # TODO: should right aligned
    offset, value = evm.stack.pop(), evm.stack.pop()
    evm.memory.store(offset, value)
    evm.pc += 1

def mstore8(evm):
    offset, value = evm.stack.pop(), evm.stack.pop()
    evm.memory.store(offset, value & 0xff)
    evm.pc += 1
