# Create a file add data and create one more file with schema and load a file using both the fies
import csv
# Crete schema file
with open("schema_file.txt",'w') as schemafile:
    writer = csv.writer(schemafile)
    writer.writerow(['Acct','Acct_type'])
