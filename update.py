import mysql.connector
import connect

def update(db):
    idd = input("ID : ")
    name = input("Nama : ")
    slug = input("Slug : ")

    sql = "UPDATE categories SET name=%s, slug=%s WHERE id=%s"
    val = (name, slug, idd)
    # val = ("Tuna", "TN", 2)

    connect.cursor.execute(sql, val)
    connect.db.commit()

    print("data " + idd + " diperbaharui")