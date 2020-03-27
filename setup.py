from cx_Freeze import setup, Executable
base = None
executables = [Executable("game.py", base=base)]
packages = ["idna", "pygame"]
include_files = ['maps', 'resources']
options = {
    'build_exe': {
        'packages':packages,
        'include_files':include_files,
    },
}
setup(
    name = "Labyrinth",
    options = options,
    version = "1.0",
    description = "Aidez MacGyver à s'échapper !",
    executables = executables
)
