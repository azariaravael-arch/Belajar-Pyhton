nama = ["Ravael","Matthew","Randy"]
#print = (nama)
print("Nama orang pertama " +nama [0])
print("Nama orang kedua " +nama [1])
print("Nama orang ketiga " +nama [2])

print("===============")

#tambah  1 data
nama.append("Valen")
print(nama)

#tambah  lebih dari 1 data
nama.extend(["Ravael","Rahel","Ismail","Wahyudi"])
print(nama)

#hapus
nama.remove("Valen")
print(nama)

#hapus lebih dari satu
del nama[0:1]
print(nama)

#edit data
nama[1] = "Imanuel"
print(nama)


#list tuple(data yang tak bisa diubah)
pelanggan = ("Yafet","Ravael","Randy","Matthew")

#list set(tak bisa menambahkan data yang sama)tidak terurut berdasarkan index

pelanggan2 = {"nama1","nama2","nama3","nama4"}

pelanggan2.add("nama5")
print(pelanggan2)

#update(sebenarnya bukan mengubah tapi menambah lebih dari 1)
pelanggan2.update(["nama6","nama7","nama8"])
print(pelanggan2)
                