from ctypes import *

num1 = 0.5
num2 = 0.8

so_file = '/Users/baesubin/Downloads/Mobify/libsub.so'
fun = cdll.LoadLibrary(so_file)
fun.substractTwoNumber.argTypes = [c_double, c_double]

print(type(fun))
print(fun.substractTwoNumber(num1, num2))

#returnValue = fun.substractTwoNumber(num1, num2)
#print(returnValue)
