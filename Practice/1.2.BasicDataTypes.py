# Python Bais Data types are : int, float, Complex num, Boolean, String
'''
int eg 10,20
Float eg 10.30
complex Num eg 3 + 5j
strin eg "chandra", "Raj"
'''

# Integer data type
integer_example = 10
print("Integer:", integer_example)

# Float data type
float_example = 10.5
print("Float:", float_example)

# String data type
string_example = "Hello, World!"
print("String:", string_example)

# Boolean data type
boolean_true = True
boolean_false = False
print("Boolean True:", boolean_true)
print("Boolean False:", boolean_false)

# Complex number data type
complex_example = 3 + 4j
print("Complex Number:", complex_example)

# Demonstrate the type of the each vairable
print("Type of integer_example:", type(integer_example))
print("Type of float_example:", type(float_example))
print("Type of string_example:", type(string_example))
print("Type of boolean_true:", type(boolean_true))
print("Type of complex_example:", type(complex_example))

# Additional Excercises for Basic Data types
import math
# Int Operation
# Absolute Value
int_num = -10
abs_val = abs(int_num)
print("Absolute Value of Integer:", abs_val)

# Power of integer 
base = 3
exponent = 4
power_result = pow(base,exponent)
print(" Power Result:" , power_result)

# 
# Float Operations
# Rounding a Float
float_num = 3.14159
rounded_num = round(float_num, 2)
print("Rounded Number:", rounded_num)

# Ceiling and Floor
print("Round of 2.5, ", round(2.5), "Round of 3.5: ", round(3.5))

float_num = 2.56
ceil_val = math.ceil(float_num)
floor_val = math.floor(float_num)
print("Ceiling Value:", ceil_val)
print("Floor Value:", floor_val)

# String Operations
# String Length
my_string = "Hello, Python!"
length = len(my_string)
print("String Length:", length)

# String to Uppercase/Lowercase
uppercase = my_string.upper()
lowercase = my_string.lower()
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)

# Boolean Operations
# Boolean Negation
bool_val = True
negated_val = not bool_val

print(negated_val,bool_val)

int_val = int(bool_val)
print("Boolean as Integer:", int_val)


# Complex Number Operations
# Complex Number Real and Imaginary Parts
complex_num = 3 + 4j
real_part = complex_num.real
imaginary_part = complex_num.imag
print("Real Part of Complex Number:", real_part)
print("Imaginary Part of Complex Number:", imaginary_part)


# Absolute Value of Complex Number
abs_val_complex = abs(complex_num)
print("Absolute Value of Complex Number:", abs_val_complex)



