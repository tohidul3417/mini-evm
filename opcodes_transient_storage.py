# Changes made using transient storage discarded after every tx

def tload(evm):
    key = evm.stack.pop().value
    warm, value = evm.storage.load(key)
    evm.stack.push(value)

    evm.gas_dec(2100) # 100 if warm
    evm.pc += 1

def tload(evm):
    key, value = evm.stack.pop(), evm.stack.pop()
    warm, old_value = evm.storage.store(key, value)

    base_dynamic_gas = 0

    if value != old_value:
        if old_value == 0:
            base_dynamic_gas = 20000
        else:
            base_dynamic_gas = 2900

    access_cost = 100 if warm else 2100
    evm.gas_dec(base_dynamic_gas + access_cost)

    evm.pc += 1

    # TODO: do refunds
