# import csv
# try:
#     with open('test.csv','w',newline="") as file:
#         writer=csv.writer(file)
#         header=['name',"contact"]
#         writer.writerow(header)
#         data=[["ram",9390581347],["sam",9390581344]]
#         writer.writerows(data)
#         print("Content added")
# except Exception as e:
#     print("Something wrong in test.csv: {e}")



#reading csv file content
# import csv
# try:
#     with open('test.csv','r') as file:
#         reader=csv.reader(file)
#         print(list(reader))
#         for row in reader:
#             print(row)
#         print("Content added")
       
# except Exception as e:
#     print("Something wrong in test.csv: {e}")

import csv
try:
    with open('test.csv', 'r') as file:
        reader = csv.reader(file)
        contacts = list(reader)
        name = input()
        new_contact = input()
        for ind, row in enumerate(contacts):
            if row[0]== name:
                contacts[ind][1] = new_contact
                break
        else:
            print("contact name nit exists")
except Exception as e:
    print(f"something wrong in test.csv: {e}")

