import pandas as pd
import dataImportAndExport
import passwordHashing

USE_SQL = False
EMPLOYEE_CSV = "employeedata"


def add_employee_data(id,column,data):
    '''takes in id number and column to put info it to add new data'''
    tempframe = dataImportAndExport.import_csv_to_dataframe(EMPLOYEE_CSV)
    tempframe.loc[id,column] = data
    print(tempframe)
    dataImportAndExport.export_csv_from_dataframe(tempframe,"employeedata")
    

def edit_data(id,column,new_data):
    '''takes in id number and column to put info it to edit new data'''
    tempframe = dataImportAndExport.import_csv_to_dataframe(EMPLOYEE_CSV)
    try:
        old_data = tempframe.loc[id,column] 
    except:
        return "edit_failure"
    tempframe.loc[id,column] = new_data
    print(tempframe)
    dataImportAndExport.export_csv_from_dataframe(tempframe,"employeedata")

def remove_user(id):
    '''removes row of data'''
    tempframe = dataImportAndExport.import_csv_to_dataframe(EMPLOYEE_CSV)
    tempframe = tempframe.drop(index=id)
    dataImportAndExport.export_csv_from_dataframe(tempframe,"employeedata")

def query_data(search_query):
    '''returns filtered frame based on search query'''
    tempframe = dataImportAndExport.import_csv_to_dataframe(EMPLOYEE_CSV)
    rows = (tempframe.applymap(lambda x: str(x).lower() == search_query)).any(axis=1)
    return tempframe.loc[rows]