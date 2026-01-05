print("")
print("KALKULATOR SEDERHANA")
print("========================")

# menu
while True:
    print("===============")
    print("==========")
    print("MENU")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("0. Keluar aplikasi")
    
    menu = input("Pilih Menu : ")
    
    if menu == "0":
        break
    elif menu == "1":
        nilai1 = float(input("Angka pertama : "))
        nilai2 = float(input("Angka kedua : "))
        hasil = nilai1 + nilai2
        print("Hasil Penjumlahan :", hasil )
    elif menu == "2":
        nilai1 = float(input("Angka pertama : "))
        nilai2 = float(input("Angka kedua : "))
        hasil = nilai1 - nilai2
        print("Hasil Pengurangan ", hasil )
    elif menu == "3":
         nilai1 = float(input("Angka pertama : "))
         nilai2 = float(input("Angka kedua : "))
         hasil = nilai1 * nilai2
         print("Hasil Perkalian :", hasil )
    elif menu == "4" :
         print("Pembagian")
         nilai1 = float(input("Angka pertama : "))
         nilai2 = float(input("Angka kedua : "))
         hasil = nilai1 / nilai2
         print("Hasil Pembagian :", hasil )
        
        
print("Matemetika ilmu yang menyenangkan😃")