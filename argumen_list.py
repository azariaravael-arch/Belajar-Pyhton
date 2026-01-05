# # #tanpa argumen list
# # def jumlah(satu,dua,tiga,empat):
# #     total = satu + dua + tiga + empat
# #     print(f"total {[satu,dua,tiga,empat]} =(total)")
    
# # jumlah(10,10,)#akan eror karena jumlah meminta 4 nilai dan hanya 2 yang terpenuhi

# #dengan argumen list
# #argumen list menggunakan tanda *
# #tidak bisa digabungkan dengan parameter lain,jadi hanya ada 1 argumen list,i jenis variable

# # def jumlahkan(*List_angka):
# #     #beri nilai awal
# #     total = 0
# #     for angka in List_angka:
# #         total = total + angka
# #     print(f"total {List_angka} = {total}")
    
# # jumlahkan(10,20,30)
# # jumlahkan(10,20,30,40,50)

# # def jumlahkan(*List_angka):
# #     #beri nilai awal
# #     total = 0
# #     for angka in List_angka:
# #         total = total + angka
# #     print(f"total {List_angka} = {total}")
    
# # jumlahkan(10,20,30)
# # jumlahkan(10,20,30,40,50)


# #PENJUMLAHAN
# # def jumlahkan(*List_angka):
# #     total = 0
# #     angkap = input("Masukan data dengan spasi : ")
# #     List_angka = [int (x) for x in angkap.split(",")]
    
# #     for angka in List_angka:
# #         if total < 0:
# #             print(f"Peringatan,{angka} kurang dari 0")
            
# #         total += angka
  
# #     print(f"total {List_angka} = {total}")
    
# # jumlahkan()
# # jumlahkan()


# def jumlahkan(*List_angka):
#     total = 0
#     angkap = input("Masukkan data dengan koma: ")
#     List_angka = [int(x) for x in angkap.split(",")]

#     # Gunakan elemen pertama sebagai nilai awal
#     total = List_angka[0]
#     for angka in List_angka[1:]:
#         total += angka

#     if total < 0:
#         print("⚠️ hasil kurang dari 0 !")

#     print(f"total {List_angka} = {total}")

# jumlahkan()
# jumlahkan()



