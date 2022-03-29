import mysql.connector

import connect

def delete(db):
    idd = input("ID : ")
    sql = 'DELETE FROM categories WHERE id=%s'
    val = (idd, )

    connect.cursor.execute(sql, val)
    connect.db.commit()

    print("data " + idd + " dihapus")

