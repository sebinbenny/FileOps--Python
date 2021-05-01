import mysql.connector
from datetime import date, datetime
import csv

try:
    mydb = mysql.connector.connect(host="", user="", passwd="", database="")
    # Change your db details as per the mysql configuration
    cursor = mydb.cursor()
    sql = "SELECT ID, NAME, PLACE FROM PERSON"
    # Write your select queries - The added one is for demo.
    cursor.execute(sql)
    res = cursor.fetchall()
    if len(res) == 0:
        print("No records found")
    else:
        ls = []
        major_ls = []
        c_date = date.today().strftime("%d%m%Y")
        c_time = datetime.now().strftime("%H%M")
        filename = 'Students Details' + c_date + '-' + c_time
        for row in res:
            pid = row[0]
            name = row[1]
            place = row[3]
            ls = [str(pid), name, place]
            major_ls.append(ls)
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerows(major_ls)

    print("WRITE COMPLETED!")
except Exception as e:
    print("An error occurred -", e)
finally:
    print("Operation Completed.")
