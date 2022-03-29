import os
import insert
import update
import list
import delete
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="kamus"
)

if db.is_connected():
    print("Berhasil terhubung ke database")

cursor = db.cursor()

def sub_menu(db):
    print("=== APLIKASI DATABASE PYTHON ===")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("0. Keluar")
    print("------------------")
    menu = input("Pilih menu> ")

    if menu == "1":
        insert.insert(db)
    elif menu == "2":
        list.list(db)
    elif menu == "3":
        update.update(db)
    elif menu == "4":
        delete.delete(db)
    elif menu == "0":
        exit()
    else:
        print("Menu Salah!")

if __name__ == "__main__":
    while(True):
        sub_menu(db)





