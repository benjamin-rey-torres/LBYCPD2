import pandas as pd
import dataImportAndExport
import passwordHashing

USE_SQL = False
TIME_CSV = "TimeinTimeout"
EMPLOYEE_CSV = "employeedata"

def log_time(time,id,type):
    temp_timedf = dataImportAndExport.import_csv_to_dataframe(TIME_CSV)
    temp_employee_df = dataImportAndExport.import_csv_to_dataframe(EMPLOYEE_CSV)
    temp_timedf.loc[str(time),["ID","TimeIn/TimeOut","Person"]] = [id,type," ".join(temp_employee_df.loc[id,["firstName","lastName"]])]
    dataImportAndExport.export_csv_from_dataframe(temp_timedf,"TimeinTimeOut")