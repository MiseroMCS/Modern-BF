import bf,sys,readline

machine = bf.Machine(memsize=8,program=input("program: "),debug_file=sys.stdout)
machine.load_libs("mathutils","dependency_manager")
machine.run()
