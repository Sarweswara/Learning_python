import random
import string

# Random number generation

# Generate Random number between 1 and 10 (it will generate one Random number between the given series)
rand_id = random.randint(9,10)
print(f"Print random integer between 9 to 10: {rand_id}")

# Generate a random float between 0 and 1 (random() doesn't take any arguments it gives some default value)
rand_float = random.random()
print("Random Float between 0 and 1:", rand_float)

# String manipulation based on random functions



# Generate a random string of specific length
length_of_string = 5
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length_of_string))
print(random_string)

print(random.choices(string.ascii_letters + string.digits, k=4))
print(''.join(random.choices(string.ascii_letters + string.digits, k=4)))

