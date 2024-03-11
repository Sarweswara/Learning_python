# Example Choosing from list of options
season_options = """
Spring,Summer,Autumn,Winter
"""
print(season_options)
#season_choice = input("Enter the number of your choice: ")
#print("You chose:", season_choice)

# practice using a list
season_guide = """
Choose your favorite season:
1. Spring
2. Summer
3. Autumn
4. Winter
"""
print(f"Please choose your seasion options: {season_guide}")
seasn_option = season_options.replace('\n','').split(',')
season_choice = seasn_option[int(input())-1]
print(f"You like {season_choice}")
print(type(season_choice))
option_for_if = season_choice
try:
    if option_for_if == 'Spring':
        
        print(f"Do you know in Spring flowers bloom.\n There is a warm wind in the spring season in the air")
    elif option_for_if == 'Summer':
        
        print(f'Do you know in Summer the hottest and brightest of the four temperate seasons,\n occurring after spring and before autumn')
    elif option_for_if == 'Autumn':
        
        print(f"Do you know this season of the year between summer and winter during which temperatures gradually decrease")
    elif option_for_if == 'Winter':
        
        print(f"Do you know this season so clod")
    else:
        print("no value choosen", option_for_if)
        print(type(option_for_if))
        print(type('Spring'))
except KeyError:
    print("wrong values given")



pet_choice = input("Enter a, b, c, or d: ").lower()
if pet_choice == 'a':
    print("You prefer dogs.")
elif pet_choice == 'b':
    print("You prefer cats.")
elif pet_choice == 'c':
    print("You prefer birds.")
elif pet_choice == 'd':
    print("You prefer fish.")
else:
    print("Invalid choice.")
