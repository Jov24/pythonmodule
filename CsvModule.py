import csv

#with open('stock_data.csv', 'r') as file:
#reader = csv.reader(file)
    #for row in reader:
        #print(row)
with open("output.csv", 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age', 'city'])
    writer.writerow(['Jovitta',19, 'Kannur'])
    writer.writerow(['James', 21, 'Kannur'])

with open("dictoutput.csv", 'w') as file:
    fieldnames = ['name','age','city']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name':'Jovita','age':19,'city':'Kannur'})
    writer.writerow({'name':'James','age':21,'city':'Kannur'})

try:
    with open('stock_data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except csv.Error as e:
    print(f'Error reading CSV file: {e}')