# Practice with JSON file

'''
{
    'Person1' : {
       'name': 'Alice', 'age': 24 
    },
    'Person2' : {
       'name': 'Jhon', 'age': 25 
    }
} 
person1['age'] = 26
'''
# JSON File
import json

with open('example.json', 'w') as file:
    json.dump({'name': ['chandra','raja'], 'age': [24,30]}, file)
with open('example.json','r') as file:
    json_var = json.load(file)
    print(json_var)

for key , val in json_var.items():
    if key == 'name':
        json_var['name'][int(input("enter the index you want to update "))]=input(' enter the desired value')
        json_var['age'][int(input("enter the desired index to update age "))]=35
        #print(json_var)
    else:
        print('no change')
 
with open('example.json', 'w') as file:
       json.dump(json_var,file)
# with open('example.json', 'r') as file:
#      final_result = json.load(file)
#      #this is the final result
#      print(final_result)
       
json_files = open('example.json','r',encoding='utf-8')
csv_reader = json.load(json_files)

def modify_dict(dict,key,valu):
     dict[key] = valu

my_dict = {'a':1,'b':2}
modify_dict(my_dict,'a',100)

print(my_dict)






#     json_var2 = json.load(file)
#     print(json_var2)
#     json_var['age'] = 25
#     print(json_var)
# with open('example.json', 'w') as file:
#     json.dump(json_var, file)
# with open('example.json', 'r') as file:
#     json_var = json.load(file)
#     print(json_var)

# Home work to update jason file create the function.
    # 3 points to cover 1) update the dictionary 2) update file 3) create function



# Perform update on the file
    