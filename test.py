#!/usr/bin/python

import ctypes

class Test(ctypes.Structure):
    _fields_ = [
        ('num' , ctypes.c_int),
        ('data', ctypes.c_char * 10)
    ]

testdll = ctypes.CDLL("./test.so")
ctest = testdll.test

test = Test()

print vars(test)
print dir(test)

ctest(ctypes.byref(test))
print (test.num)
print "From python: " + test.data.decode("utf-8")

