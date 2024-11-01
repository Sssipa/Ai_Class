
x = [1,3,4,5,8,9,3,10,1,3,5,6,8,3,5,7,4,3,5,6]
y1 = int(input("Masukkan nilai: "))

if y1 % 2 == 0:
    if y1 in x:
        print(f"Ditemukan pada indeks ke-{x.index(y1)}")
    else:
        print("Hasil tidak ditemukan.")
else:
    if y1 not in x:
        print("Hasil tidak ditemukan.")
