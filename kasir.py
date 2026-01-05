print("================================")
print("================================")
print("Selamat datang ditoko buku Ravael")

produk = input("Masukan produk : ")
harga = float(input("Masukan harga : "))
diskon = float (input("Masukan diskon : "))

potongan = harga * (diskon /100)
total = harga - diskon

print("========== rincian pesanan ==========")

print(f"Produk : {produk}.")
print(f"Harga : {harga}.")
print(f"Diskon : {diskon}.")
print(f"Total : {total}.")

