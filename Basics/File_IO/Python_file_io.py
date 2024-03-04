# Python file IO

import csv


# CSV File
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age','city'])
    writer.writerow(['Alice', 24,'Chennai'])
    writer.writerow(['Bob', 19,'Vijaiwada'])
with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        for col in row:
            print(col)

# Need to take input file Tital first number second number as 2 cols read each of the number and add sum into new file
            
with open('input.csv','w+',newline='') as infile:
    writer = csv.writer(infile)
    writer.writerow(['First_num','second_num'])
    writer.writerow([1,5])
    writer.writerow([10,15])

with open('output.csv','w',newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['First_num','second_num','sum'])

csv_file = open('input.csv','r',encoding='utf-8')
csv_reader = csv.reader(csv_file,delimiter=',')
next(csv_reader,None)

for row in csv_reader:
    first_num,second_num = row
    sum = int(first_num) + int(second_num)
    with open('output.csv','a',newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow([first_num,second_num,sum])
    


