# Python input statement

# Python input() function example

# Basic input
#name = input("Enter your name ")
#print("Hello ",  name + "!")
from datetime import datetime 
# Enter a with int input
#age = int(input("Enter the age "))
current_datetime = datetime.now()
#print("you are", age ,"old!")


# Input with prompt for a float
#height = float(input("Enter your height in meters: "))
#print("Your height is", height, "meters.")


# Boolean input
# Python doesn't have a built-in way to input booleans, so we use a string and compare
likes_python = input("Do you like Python? (yes/no): ").lower() == "yes"
#print("Likes Python:", likes_python)



# Handling input errors with try-except
try:
   # number = float(input("Enter a number :")) # Using float to accept both integers and floats
    number = 1
    print(number)
except ValueError:
    print("This is not a valid number :")

# Find year of birht of a person
from datetime import datetime 
try:
    age = int(input("Enter the Age :"))
    current_datetime = datetime.now()
    find_dob_year = current_datetime.year - age
    print(f"You born on {find_dob_year}")
except ValueError:
    print("Wrong format given expected value is int")

# Taking the entire value as list
number_list = input().split()
print(number_list)



    