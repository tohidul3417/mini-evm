def _pop(evm):
    evm.pc += 1
    evm.gas_dec(2)
    evm.stack.pop(0)
