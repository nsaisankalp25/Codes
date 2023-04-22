import os, csv
print(__file__)
a = __file__
a = a.split("\\")[:-1]
a = "\\".join(a)
print(a)
os.chdir(a)
print(os.getcwd())
print(os.listdir())

#with open(os.getcwd() + r'\Dependencies\EmployeeDB.csv') as file:
#    for i in csv.reader(file):
#        print(i)
print("Python is the best")
