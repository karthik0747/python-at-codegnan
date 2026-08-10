import csv
try:
    with open('test.csv','r') as file:
        reader=csv.reader(file)
        print(list(reader))
        for row in reader:
            print(row)
        print("Content added")
       
except Exception as e:
    print("Something wrong in test.csv: {e}")
