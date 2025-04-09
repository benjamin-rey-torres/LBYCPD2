import passwordHashing
import dataImportAndExport
import ast
EMPLOYEE_CSV = "employeedata"

def verify_valid_user(input_user,input_pass):
    '''this function determines if a input username and password is valid
    it will return different stirngs depednding on the result'''
    #import employee data
    tempframe = dataImportAndExport.import_csv_to_dataframe(EMPLOYEE_CSV)
    #check if user is valid
    user_valid = (tempframe['username'].eq(input_user)).any()
    if user_valid == False:
        return "invalid username"
    #gets user number if user is valid
    user_number = tempframe[tempframe['username'].str.contains(input_user)].index[0]
    # uses password hashing check to see if password is correct
    if passwordHashing.checkHashPass(input_pass,ast.literal_eval(tempframe.loc[user_number,"passwordHash"])):
        return "valid credentials"
    else:
        return "incorrect password"
    

print(verify_valid_user("username23","check123"))
