import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": [], "include_files": ["views/", "images/", "requirements.txt"]}

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name="marielos",
    version="0.1",
    description="descargar música",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)
