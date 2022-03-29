pak_tani = {
    "nama": "Petani Kode",
    "umur": 22,
    "hobi": ["coding", "membaca", "cocok tanam"],
    "menikah": False,
    "sosmed": {
        "facebook": "petanikode",
        "twitter": "@petanikode"
    }
}

print("Nama Pak Tani adalah " + pak_tani["nama"])
print("Umur Pak Tani adalah " + str(pak_tani["umur"]))
print("Hobi Pak Tani ada " + str(len(pak_tani["hobi"])))
count = 0
for i in pak_tani["hobi"]:
    count += 1
    print(str(count) + ". " + str(i))

status = pak_tani["menikah"]

if pak_tani["menikah"] == status:
    print("Status pak tani adalah : Belum Menikah")
else:
    print("Status pak tani adalah : Menikah")

print("FB Pak tani adalah : " + pak_tani["sosmed"]["facebook"])
print("Twitter Pak tani adalah : " + pak_tani["sosmed"]["twitter"])