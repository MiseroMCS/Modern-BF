import bf
import sys

def base_right(machine): #char > from vanilla BF.
    if(machine.pointer+1 < len(machine.memory)): #check to make sure you don't go beyond the end of the tape. Returns an unrecoverable error if you try.
        machine.pointer += 1
        return 0
    return 1

def base_left(machine): #char < from vanilla BF.
    if(machine.pointer-1 >= 0): #check to make sure you don't go beyond the end of the tape. Returns an unrecoverable error if you try.
        machine.pointer -= 1
        return 0
    return 1

def base_add(machine): #char + from vanilla BF.
    machine.memory[machine.pointer] += 1
    return 0

def base_sub(machine): #char - from vanilla BF.
    if(machine.memory[machine.pointer]-1 < 0):
        return 1
    machine.memory[machine.pointer] -= 1
    return 0

def base_out(machine): #char . from vanilla BF.
    sys.stdout.write(chr(machine.memory[machine.pointer]))
    sys.stdout.flush()
    return 0

def base_in(machine): #char , from vanilla BF.
    machine.memory[machine.pointer] = ord(bf.input_char())
    return 0

def base_open_loop(machine): #char [ from vanilla BF.
    machine.loops.append(machine.memory[0]-1)
    return 0

def base_close_loop(machine): #char ] from vanilla BF.
    if(machine.memory[machine.pointer] != 0):
        jump = machine.loops.pop()
        machine.memory[0] = jump
    return 0

def get_name(machine):
    return "Vanilla BF"

def imported(machine): #initializes needed variables in machine.
    machine.loops = []

def get_chars(machine): #gives the required characters for the library
    return {"<":base_left,">":base_right,"+":base_add,"-":base_sub,".":base_out,",":base_in,"[":base_open_loop,"]":base_close_loop}

def debug_info(machine):
    return "Char: {}, Pointer:{}, Loops:{}, Memory:{}".format(machine.get_current_char(), machine.pointer, machine.loops, machine.memory)
