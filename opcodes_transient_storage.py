# Changes made using transient storage discarded after every tx

def tload(evm):
    key = evm.stack.pop().value
    warm, value = evm.storage.load(key)
    evm.stack.push(value)

    evm.gas_dec(100)
    evm.pc += 1

def tstore(evm):
    key, value = evm.stack.pop(), evm.stack.pop()
    evm.storage.store(key, value)
    evm.gas_dec(100)
    evm.pc += 1

