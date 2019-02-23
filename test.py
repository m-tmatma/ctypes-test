#!/usr/bin/python

import ctypes

class Test(ctypes.Structure):
    _pack_ = 2
    _fields_ = [
        ('a' , ctypes.c_char),
        ('b' , ctypes.c_short),
        ('c' , ctypes.c_int),
        ('num' , ctypes.c_int),
        ('data', ctypes.c_char * 10)
    ]

testdll = ctypes.CDLL("./test.so")
ctest = testdll.test

test = Test()

print (vars(test))
print (dir(test))

ctest(ctypes.byref(test))
print ("a = ", test.a)
print ("b = ", test.b)
print ("c = ", test.c)
print ("num = ", test.num)
print ("From python: " + test.data.decode("utf-8"))

