def bf_call(machine):
    call_id = machine.memory[machine.pointer]
    if(call_id >= len(machine.calls)):
        return 1
    machine.calls[machine.memory[machine.pointer]](machine)
    return 0

def get_chars(machine):
    return {"^":bf_call}

def imported(machine):
    machine.calls = []
    for imported in machine.loaded_libs:
        if(hasattr(imported,"get_calls")):
            machine.calls += imported.get_calls(machine)
