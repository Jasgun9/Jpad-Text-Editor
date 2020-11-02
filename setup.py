import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"D:\Python38-32\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"D:\Python38-32\tcl\tk8.6"

executables = [cx_Freeze.Executable("Jpad.py", base=base, icon="icon.ico",  )]

cx_Freeze.setup(
    name = "Jpad Text Editor",
    author = "Jasgun Singh",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icon.ico",'tcl86t.dll','tk86t.dll', 'icons2'], }},
    version = "0.01",
    description = "This is a normal text editor. Made by Jasgun singh in python 3.8.5. Tkinter Application",
    
    executables = executables
    )
