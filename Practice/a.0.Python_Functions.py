# Python Function Basics

# Define a simple function to great
def greet():
    print("Hello")

# Calling Function
greet()

# Define a functin with parameter
def greet_person_name(name):
    print(f"Hi {name}")

# Calling function with parameter
greet_person_name('Chandra')

# Function with return value
def add_number(a,b):
    return a + b

result = add_number(5,6)
print(result)

# Function with default parameters
def default_parms(name='Friend'):
    return name


print(f"Me and my  {default_parms('Chandra')} went to shop")

