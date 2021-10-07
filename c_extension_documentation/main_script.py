from ctypes import CDLL

adder_test = CDLL('./test_shared.out')

# Using a C Function.
output_c = adder_test.a_c_function()
print(output_c)

# Using another C Funciton.
adder_test.main()
