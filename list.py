import mysql.connector
import connect

def list(db):
    sql = "SELECT * FROM categories"
    connect.cursor.execute(sql)

    data = connect.cursor.fetchall()
    count = 0
    for datas in data:
        count += 1
        # print(datas)
        print(str(count) + ". " + datas[1] + "(" + datas[2] + ")" + "->" + "ID : " + str(datas[0]))
