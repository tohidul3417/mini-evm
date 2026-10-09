import time
import random

def address(evm):
    evm.stack.push(evm.sender)
    evm.pc += 1
    evm.gas_dec(2)

# here just mocking this
def balance(evm):
    address = evm.stack.pop()
    evm.stack.push(9999999999999)

    evm.pc += 1
    evm.gas_dec(2600) # 100 if warm

# The address that originally triggered the execution. This is tx.origin in Solidity.
# For us tx.origin is always equal to msg.sender. That is why we simply return the sender.
def origin(evm):
    evm.stack.push(evm.sender)
    evm.pc += 1
    evm.gas_dec(2)

def caller(evm):
    evm.stack.push("0x414b60745072088d013721b4a28a0559b1A9d213")
    evm.pc += 1
    evm.gas_dec(2)

def callvalue(evm):
    evm.stack.push(evm.value)
    evm.pc += 1
    evm.gas_dec(2)

# Pushed the current input data (32 bytes) on the stack
def calldataload(evm):
    i = evm.stack.pop()

    delta = 0
    if i+32 > len(evm.calldata):
        delta = i+32 - len(evm.calldata)

    # always has to be 32 bytes
    # if it is not we append 0x00 bytes until it is
    calldata = evm.calldata[i:i+32-delta]
    calldata += 0x00*delta

    evm.stack.push(calldata)
    evm.pc += 1
    evm.gas_dec(3)

def calldatasize(evm):
    evm.stack.push(len(evm.calldata))
    evm.pc += 1
    evm.gas_dec(2)

# stores a specified part of the calldata in memory
def calldatacopy(evm):
    destOffset = evm.stack.pop()
    offset = evm.stack.pop()
    size = evm.stack.pop()

    calldata = evm.calldata[offset:offset+size]
    memory_expansion_cost = evm.memory.store(destOffset, calldata)

    static_gas = 3
    minimum_word_size = (size + 31) // 32
    dynamic_gas = 3 * minimum_word_size + memory_expansion_cost

    evm.pc += 1
    evm.gas_dec(static_gas + dynamic_gas)

def codesize(evm):
    evm.stack.push(len(evm.program))
    evm.pc += 1
    evm.gas_dec(2)

def codecopy(evm):
    destOffset = evm.stack.pop()
    offset = evm.stack.pop()
    size = evm.stack.pop()

    code = evm.program[offset:offset+size]
    memory_expansion_cost = evm.memory.store(destOffset, code)

    static_gas = 3
    minimum_word_size = (size + 31) // 32
    dynamic_gas = 3 * minimum_word_size + memory_expansion_cost

    evm.pc += 1
    evm.gas_dec(static_gas + dynamic_gas)

# The current gas price.
# Because we are running everything locally, the gas price is simply 0
def gasprice(evm):
    evm.stack.push(0x00)
    evm.pc += 1
    evm.gas_dec(2)

# The size of another program given by its address.
# There are no other programs in our simplified world so we simply return 0.
def extcodesize(evm):
    address = evm.stack.pop()
    evm.stack.push(0x00)
    evm.pc += 1
    evm.gas_dec(2600) # 100 if warm

# Stores a specified part of another program in memory
def extcodecopy(evm):
    address    = evm.stack.pop()
    destOffset = evm.stack.pop()
    offset     = evm.stack.pop()
    size       = evm.stack.pop()

    extcode = [] # no external code
    memory_expansion_cost = evm.memory.store(destOffset, extcode)

    # refactor this in separate method
    minimum_word_size = (size + 31) / 32
    dynamic_gas = 3 * minimum_word_size + memory_expansion_cost
    address_access_cost = 100 # if warm else 2600

    evm.pc += 1
    evm.gas_dec(dynamic_gas + address_access_cost)

# Get size of output data from the previous call from the current environment.
# As our execution is the only one running, there is no previous return data.
# Therefore we can simply return 0.
def returndatasize(evm):
    evm.stack.push(0x00) # no return data
    evm.pc += 1
    evm.gas_dec(2)

def returndatacopy(evm):
    destOffset = evm.stack.pop()
    offset = evm.stack.pop()
    size = evm.stack.pop()

    returndata = evm.returndata[offset:offset+size]
    memory_expansion_cost = evm.memory.store(destOffset, returndata)

    minimum_word_size = (size + 31) // 32
    dynamic_gas = 3 * minimum_word_size + memory_expansion_cost

    evm.pc += 1
    evm.gas_dec(3 + dynamic_gas)

# The hash of another program given by its address.
# There are no other programs in our simplified world so we simply return 0.
def extcodehash(evm):
    address = evm.stack.pop()
    evm.stack.push(0x00) # no code

    evm.gas_dec(2600) # 100 if warm
    evm.pc += 1

# Get the hash of one of the 256 most recent complete blocks and push it on the stack.
# Cannot be used as a source of randomness due to it being susceptible to manipulation by validators.
def blockhash(evm):
    blockNumber = evm.stack.pop()
    if blockNumber > 256:
        raise Exception("Only last 256 blocks can be accessed")
    evm.stack.push(0xe8f2ee36e9753aff942b6e3017a833e0c82229d8ddc392db7466627df80d6504)
    evm.pc += 1
    evm.gas_dec(20)

# Get the address of the validator proposing this block.
def coinbase(evm):
    evm.stack.push(0x396343362be2A4dA1cE0C1C210945346fb82Aa49)
    evm.pc += 1
    evm.gas_dec(2)

def timestamp(evm):
    now = int(time.time())
    now -= now % 12
    evm.stack.push(now)
    evm.pc += 1
    evm.gas_dec(2)

def prevrandao(evm):
	# Should be from the previous block's mixHash, such as:
	# prevMixHash = prevBlock.mixHash
	# prevMixHash = 0xaeaec252beafe3fd35a11bdc5e3c71925f2e9e01472b7a2a290dc4619f645206
	# here we use random int
	prevMixHash = random.randint(0, 2 ** 256 - 1)
	return prevMixHash

