# Print statement practice
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''This another String definition: Hello there!''')

single_line_text = "this is a single line text"
multi_line_text = """
This is multi-line text
having
line1
line2
line3
I love Python programming
"""

another_multi_line_text = '''
This is multi-line text
having
line1
line2
line3
I love Python programming
'''
print(single_line_text)
print(multi_line_text)

# Basic print to console
print("Hello world!\n")

# Formatted print using .format()
name = 'Anjali'
print("Hello, {}!" .format(name))

# Formated pring using f-string (python 3.6 and above)
age = 30
print(f"{name} is {age} years old")

# Print multiple items and multple data types
print("Name :", name , "- Age", age)

# Writing to a file
with open("output.txt",'w') as file:
    file.write("Hello World!\n")
    file.write("Hello, {}!" .format(name))
    file.write(f"{name} is {age} years old\n")
    file.write(f"Name: {name} - Age : {age}\n")

with open("onemore.txt" ,'w') as newfile:
    newfile.write("Hello World\n")
    newfile.write("Hello, {}! World!\n")
    newfile.write(f"{name} is {age} years old\n")
    newfile.write(f"name: {name} - Age : {age}\n")


# Print with a seperator
print("Apple", "Banana", "Cherry", "Pineapple", "Guva", sep=' ')

# Printing with end seperator
print("This is in\n one line ", end=',')
print("And this continues in the same\n line")

# writing a list to a file with join
fruits = ["Apple","Banana","Cherry"]
with open("fruits.txt",'w') as file:
    file.write(",".join(fruits))


places = ["HYD","Chennai","Bang"]
with open("places.txt",'w') as placefile:
    placefile.write(",".join(places))


# Printing with commas, mixing data types, and using expressions
    # Basic Variable with different data types
    name = "Jhon"
    age = 32
    height = 5.8 # in feet

    # Basic print with comma seperation
    print("Name:",name, "Age:",age,"Height:" , height)

    # Printing with expression
    print("In ten years,",name,"will be",age + 10 , "years old.")

    # Printing with data types
    is_student = False
    is_employee = True
    print(name, "is a student:", is_student)
    print(name, "is an employee:", is_employee)

    # Using Mathematica expressions
    number_of_apples = 5
    number_of_oranges = 10
    number_of_mangoes = 30
    print("Total Fruits :", number_of_apples + number_of_oranges + number_of_mangoes)

    # Printing with mix of strings and numbers
    print(name, "is", age, "years old and" , height , "feet tall")
    
    # Define a float number
    float_number = 3.1435669

    # Round of 2 Decimal values
    rowunded_two = round(float_number,2)
    print("Rounded with 2 decimal places:", rowunded_two)
    # Round of 4 Decimal values
    round_four = round(float_number,4)
    print("Rounded to 4 decimal palces:", round_four)

    # Rounded to no Decimal places(integer)
    rounded_no_decimal = round(float_number)
    print("Rounded to no decimal places:" , rounded_no_decimal)

    # New line
    print("Hello\nworld")

    # Tab
    print("Hello\twolrd")

    # Backslash
    print("This is backslash: \\")

    # Single quote
    print('It\'s a sunny day')

    # Doubble quote
    print("He said, \"Hello!\"")
    print("He said, \"Hi\"")
    
    # Carriage return
    print("Hello\rworld") 

    # Back space
    print("Hello\bworld")
    # From Feed
    print("Hello\fworld") 
    # Octal Value
    print("\o12")
    print("\o12")  #why is this not giving a new lie

    print("\x0a")
    print("\u2764")

    # Print Date time
    from datetime import datetime
    current_datetime = datetime.now()
    print(current_datetime)
    print("Current Date time now:" , current_datetime)
    # Print individual components (year, month, day, hour, minute, second)
    print("Year:",end='')
    print(current_datetime.year,"\n",current_datetime.month,current_datetime.day, sep='-')
print("Month:", current_datetime.month)
print("Day:", current_datetime.day)
print("Hour:", current_datetime.hour)
print("Minute:", current_datetime.minute)
print("Second:", current_datetime.second)


