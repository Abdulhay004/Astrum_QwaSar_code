import sqlite3 as sql
import csv
import pandas as pd

def sql_to_csv(database, table_name):
    
    conenction = sql.connect(database)
    cursor = conenction.cursor()
    cursor.execute(f'SELECT * FROM {table_name}')
    header = []
    for i in cursor.description:
        header_ele=i[0]
        header.append(header_ele)

    with open('volcano.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for each in cursor:
            writer.writerow(each)
    with open('volcano.csv', 'r') as file:
        return file.read().rstrip()



def csv_to_sql(csv_content, database, table_name):
    connection = sql.connect(database)
    df = pd.read_csv(csv_content)
    df.to_sql(table_name, connection, if_exists='append', index=False)
