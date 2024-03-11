
season_options = """Spring,Summer,Autumn,Winter"""

seasn_option = season_options.split(',')
print(seasn_option)
season_choice = seasn_option[int(input())-1]
print(f"You like {season_choice}")
print(type(season_choice))
option_for_if = season_choice

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
