import sys

def multiply(machine):
    machine.memory[machine.pointer] *= 2
    return 0

def itoa(machine):
    sys.stdout.write(str(machine.memory[machine.pointer]))
    sys.stdout.flush()
    return 0

def get_chars(machine):
    return {"*":multiply,"%":itoa}
