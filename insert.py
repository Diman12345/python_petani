import mysql.connector
import connect

# single data
# name = input("Nama : ")
# slug = input("Slug : ")
# sql = "INSERT INTO categories (name, slug) VALUES (%s, %s)"
# val = (name, slug)
# cursor.execute(sql, val)
#
# db.commit()
# print("{} data ditambahkan".format(cursor.rowcount))

# Multi data
def insert(db):
    banyak = input("Berapa banyak Kategori Input : ")
    count = 0
    val = []
    for i in range(int(banyak)):
        count += 1
        inputan_nama = input("Nama Kategori ke-" + str(count) + ". ")
        inputan_slug = input("Slug Kategori ke-" + str(count) + ". ")
        value = (inputan_nama, inputan_slug)
        val.append(value)

    sql = "INSERT INTO categories (name, slug) VALUES (%s, %s)"

    for item in val:
        connect.cursor.execute(sql, item)
        connect.db.commit()

    print("{} data ditambahkan".format(len(val)))