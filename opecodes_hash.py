def sha3(evm):
    offset, size = evm.stack.pop(), evm.stack.pop()
    value = evm.memory.access(offset, size)
    evm.stack.push(hash(str(value)))

    evm.pc += 1

    # calculate gas
    minimum_word_size = (size + 31) / 32
    dynamic_gas = 6 * minimum_word_size # TODO: + memory_expansion_cost
    evm.gas_dec(30 + dynamic_gas)
