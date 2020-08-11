import cx_Freeze

executables = [cx_Freeze.Executable('main.py')]

cx_Freeze.setup(
    name='Sokoban',
    options = {"build_exe": {"packages":["pygame"],
                             "include_files":["resources/images/character (Mini) (Custom).png", "resources/images/box.png"]}},
    executables = executables
)