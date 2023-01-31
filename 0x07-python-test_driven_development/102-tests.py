import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_string.argtypes = [ctypes.py_object]
s = "The spoon does not exist"
lib.print_python_string(s)
s = "????? ?? ??????????"
lib.print_python_string(s)
s = "La cuillère n'existe pas"
lib.print_python_string(s)
s = "?????"
lib.print_python_string(s)
s = "???? ???? ???."
lib.print_python_string(s)
s = "??????????"
lib.print_python_string(s)
s = b"The spoon does not exist"
lib.print_python_string(s)
