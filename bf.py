import sys
import curses
import time

def input_char(): #thanks user2660966 on StackOverflow for this hacky fix. Made slight modification.
    try:
        win = curses.initscr()
        while True:
            ch = win.getch()
            #if ch in range(32, 127): break
            break
            time.sleep(0.05)
    except: raise
    finally:
        curses.endwin()
    return chr(ch)

class Machine(object):
    def __init__(self, memsize=1024, program="", debug_file=None):
        self.program = program
        self.memory = [0 for x in range(memsize)]
        self.chars = {}
        self.pointer = 0
        self.debug_file = debug_file
        self.loaded_libs = []
        self.load_libs("vanilla_bf")
    def load_libs(self, *kwargs):
        for filename in kwargs:    
            imported = getattr(__import__("libs." + filename),filename)
            if(hasattr(imported, "imported")):
                imported.imported(self)
            if(hasattr(imported, "get_chars")):
                self.chars.update(imported.get_chars(self))
            self.loaded_libs.append(imported)
    def load(self, program):
        self.program = program
        self.memory[0] = 0
    def get_current_char(self):
        try:
            return self.program[self.memory[0]]
        except IndexError:
            sys.exit(print("Invalid instruction pointer."))
    def run(self):
        if(self.debug_file):
            self.debug_file.write("Starting Memory: {}\n".format(self.memory))
        for imported in self.loaded_libs:
            if(hasattr(imported, "prerun")):
                imported.prerun(self)
        while(self.memory[0] < len(self.program)):
            char = self.get_current_char()
            if(char in self.chars.keys()):
                response = self.chars[char](self)
                if(self.debug_file):
                    for imported in self.loaded_libs:
                        if(hasattr(imported, "debug_info") and hasattr(imported, "get_name")):
                            self.debug_file.write("{}: {}\n".format(imported.get_name(self),imported.debug_info(self)))
                if(response):
                    continue
                    print("Unrecoverable error at column {}.".format(self.memory[0]))
                    print(self.program)
                    print((" "*(self.memory[0]-1)) + "^")
                    sys.exit(1)
            else:
                print("Error: Unrecognized character '{}' at column {}.".format(char,self.memory[0]))
                sys.exit(1)
            self.memory[0] += 1
        if(self.debug_file):
            self.debug_file.write("Final Memory: {}\n".format(self.memory))
        self.memory[0] = 0
        for imported in self.loaded_libs:
            if(hasattr(imported, "postrun")):
                imported.postrun(self)
