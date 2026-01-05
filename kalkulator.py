# Kalkulator Sederhana

print("=== Kalkulator Sederhana ===")

# Ambil input dari user

angka1 = float(input("Masukkan angka pertama: "))

operator = input("Pilih operator (+ | - | * |  / ): ")
angka2 = float(input("Masukkan angka kedua: "))

# Proses operasi
if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        hasil = "Error: Tidak bisa bagi 0!"
else:
    hasil = "Operator tidak dikenali!"

# Tampilkan hasil
print("Hasil:", hasil)

