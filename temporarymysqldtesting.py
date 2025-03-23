# import mysql.connector
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

#string to connect to database
con_string = 'mysql://root:test123@localhost/weareitsampledatabase'
engine = create_engine(con_string)

# select employee table
query = """
    SELECT *
    FROM employees e
"""

# read empolyee table
df_read_sql = pd.read_sql(query,engine,index_col="id")

# add column with firstname intials
df_read_sql["firsname_initial"] = df_read_sql["firstName"].astype(str).str[0]

# sort by last name
df_read_sql = df_read_sql.sort_values(by="lastName")

# print result
print(df_read_sql)

