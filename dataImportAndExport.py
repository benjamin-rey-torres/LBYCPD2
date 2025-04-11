import pandas as pd

def import_csv_to_dataframe(spreadsheet_name):
    """function that takes in a csv file name to return a pandas dataframe (esentially a table)
    to do functions on"""
    dataframe = pd.read_csv(f"{spreadsheet_name}.csv",index_col=0)
    return dataframe

def export_csv_from_dataframe(dataframe_name,csv_filename):
    """function that takes in a current dataframe to be exported into a csv file"""
    dataframe_name.to_csv(f"{csv_filename}.csv")


# Test case, uncomment to try
# reads csv
# if __name__ == "__main__":
#     temp_df = import_csv_to_dataframe("testsheet")

#     # makes new column that takes first letter of
#     temp_df['first_name_initial'] = temp_df['firstName'].astype(str).str[0]

#     # sort by last name
#     export_csv_from_dataframe(temp_df,"testsheet2")


