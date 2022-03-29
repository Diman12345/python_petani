x = 5
item = ["nasi", "micin", "telur"]

print("X terdiri dari " + str(x) + " bilangan, yaitu :")

for i in range(x):
    print("bilangan ke " + str(i+1))

print("Menu yang tersedia ada " + str(len(item)))

for items in item:
    print("Daftar menu : " + items)