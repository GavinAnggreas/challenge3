print ("<<\tIdentifikasi bilangan\t>>")
print("identifikasi nilai jika nilai 10 - 15 atau")
print ("nilai 20 - 25 atau 35 - 40")
print("-"*30)
x = int(input("Masukkan bilangan :"))
while (10 < x < 15 or 20 < x < 25 or 35 < x < 40):
    print ("Benar...")
    break
while ( x < 10 or 15 < x < 20 or 25 < x < 35 or 35 < x < 40):
    print("SALAH!")
    x = int(input("Masukkan bilangan :"))