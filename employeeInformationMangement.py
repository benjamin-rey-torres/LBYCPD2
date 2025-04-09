import pandas as pd
import dataImportAndExport
import passwordHashing

USE_SQL = False
EMPLOYEE_CSV = "employeedata"


def add_employee_data(id,column,data,type=None):
    tempframe = dataImportAndExport.import_csv_to_dataframe(EMPLOYEE_CSV)
    tempframe.loc[id,column] = data
    print(tempframe)
    dataImportAndExport.export_csv_from_dataframe(tempframe,"employeedata")
    

# def edit_data():

# def remove_data():

# def query_data():

add_employee_data(1,"salary",70000)
add_employee_data(1,"username","username123")
add_employee_data(1,"passwordHash",passwordHashing.returnHashPass("test123"))
add_employee_data(2,"salary",40000)
add_employee_data(2,"username","username23")
add_employee_data(2,"passwordHash",passwordHashing.returnHashPass("check1234"))
add_employee_data(3,"salary",100000)
add_employee_data(3,"username","username56")
add_employee_data(3,"passwordHash",passwordHashing.returnHashPass("yes54321"))
add_employee_data(4,"salary",10000)
add_employee_data(4,"username","username78")
add_employee_data(4,"passwordHash",passwordHashing.returnHashPass("password123"))
add_employee_data(5,"salary",20000)
add_employee_data(5,"username","username92")
add_employee_data(5,"passwordHash",passwordHashing.returnHashPass(""))