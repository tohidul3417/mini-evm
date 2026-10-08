UINT_256_MAX = (1 << 256) - 1
UINT_255_NEGATIVE_ONE = UINT_256_MAX

def byte(evm):
    i, x = evm.stack.pop(), evm.stack.pop()
    if i >= 32:
        result = 0
    else:
        result = (x // pow(256, 31 - i)) % 256
    evm.stack.push(result)
    evm.pc += 1
    evm.gas_dec(3)

def shl(evm):
    shift, value = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(value << shift)
    evm.pc += 1
    evm.gas_dec(3)

def shr(evm):
    shift, value = evm.stack.pop(), evm.stack.pop()
    evm.stack.push(value >> shift)
    evm.pc += 1
    evm.gas_dec(3)

# signed shift right
def sar(evm):
    shift, value = evm.stack.pop(), evm.stack.pop()

    if shift >= 256:
        result = 0 if (value >> 255) == 0 else UINT_255_NEGATIVE_ONE
    else:
        if value & (1 << 255): # where 1 << 255 is 100......00
            signed_value = value - (1 << 256) # makes the value signed from unsigned
        else:
            signed_value = value

        shifted = signed_value >> shift
        result = shifted & UINT_256_MAX

    evm.stack.push(result)
    evm.pc += 1
    evm.gas_dec(3)
