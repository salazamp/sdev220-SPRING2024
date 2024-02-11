# 16.8 Use the sqlalchemy module to connect to the sqlite3 database books.db 


from sqlalchemy import *

import pandas as pd

data=sqlalchemy.create_engine('sqlite:////path/books.db')

#select and print the title column from the book table in alphabetical order.
df=pd.read_sql('select title from book',data)

print(df)