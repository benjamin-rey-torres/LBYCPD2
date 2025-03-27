import pandas as pd
import dataImportAndExport
import passwordHashing

USE_SQL = False
EMPLOYEE_CSV = "employeedata"


def add_data(id,column,data,type=None):
    tempframe = dataImportAndExport.import_csv_to_dataframe(EMPLOYEE_CSV)
    tempframe.loc[id,column] = data
    print(tempframe)
    dataImportAndExport.export_csv_from_dataframe(tempframe,"employeedata")
    

# def edit_data():

# def remove_data():

# def query_data():

add_data(1,"salary",70000)
add_data(1,"username","username123")
add_data(1,"passwordHash",passwordHashing.returnHashPass("test123"))