import csv, os
info_msg = """
        
        Employee DB Manager is an application which manages the
        information about the companys employee information.
        Created & Developed by:  Sai Sankalp
        Version 0.9.8: Pre-Release Stage
        Features: Add, Load and Delete Employees Information
        How to use:
        >> Click on the load button to load brief information about all employees
        >> Click on Add button to Add employees information [
            ^* SN: Number
            ^* ID: Number (25125xxx)
            ^* Name: Full Name
            ^* Age: Number
            ^* Gender: M/F
            ^* Sector/Field: Operations/Finance/Development etc
            ^* Date of Joining: dd/mm/yy
            ^* Salary: Number (without short Forms, currency: INR)
            ^* Access Level: A/B/C (A>B>C)
            ^* Award/achievements: Mention Full name / NA
            ^* Other Info about the person: Brief Info / NA ]
        >> Database: CSV file
        >> Developed in: Python 3.x
        >> UI: Tkinter
        """
a = "\\".join(__file__.split("\\")[:-1])
os.chdir(a)
FilePath = os.getcwd() + '\EmployeeDB.csv'
print(FilePath)
EmployeeInfoList = []

def FilePresenceCheck():
    os.chdir(a)

    def FolderPresence():        
        if "Dependencies" not in os.listdir():
            os.mkdir(os.getcwd() + r'\Dependencies')
            globals()["FilePath"] = os.getcwd() + r'\Dependencies'
            os.chdir(FilePath)
        else:
            globals()["FilePath"] = os.getcwd() + r'\Dependencies'
            os.chdir(FilePath)
    FolderPresence()

    if "EmployeeDB.csv" not in os.listdir():
        with open(FilePath + r'\EmployeeDB.csv', 'w') as file:
            main_info = ["PythonForKids", "PythonForKids.net",   "Sai Sankalp", "05/08/2021", "15000"]
            obj = csv.writer(file, lineterminator='\n')
            obj.writerow(main_info)
            obj.writerow("SN, ID, NAME, AGE, GENDER, SECTOR, ROLE, DATE OF JOINING, SALARY, A/B/C LEVEL ACCESS, AWARDS/ACHIEVEMENTS, OTHER INFO".split(","))
            EmployeeInfoList.append("NONE")
    else:
        with open(FilePath + r'\EmployeeDB.csv', 'r') as file:
            content = csv.reader(file)
            for i in content:
                EmployeeInfoList.append([ii.strip() for ii in i])

def erase_func():
    EmployeeInfoList.clear()

class DB:
    def EmployeeInfo():
        return EmployeeInfoList

    def CompanyInfo():
        return EmployeeInfoList[0]

    def EmployeeInfoParam():
        return EmployeeInfoList[1]

    def AddEmployeeInfo(a:list):
        with open(FilePath + r'\EmployeeDB.csv', 'a') as file:
            csv.writer(file, lineterminator='\n').writerow(a)