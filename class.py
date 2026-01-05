# class Person :
#     #inisialisasi
#     def __init__(self, first_name, last_name):
#         self.nama_depan = first_name
#         self.nama_belakang = last_name
        
#     def full_name(self):
#         return f"Hallo, {self.nama_depan} {self.nama_belakang} 😃"
    
# person1 = Person("Ravael","Rompas")
# person2 = Person("Randy","Yandeday")

# print(person1.full_name())
# print(person2.full_name())


# class Ravael :
#     #inisialisai
#     def __init__(self,Nama,Jurusan,Kelas):
#         self.Nama = Nama
#         self.Jurusan = Jurusan
#         self.Kelas = Kelas
        
#     def siswa(self):
#         return f"Nama :{self.Nama} Kelas : {self.Kelas} Jurusan :{self.Jurusan}"
    
# person1 = Ravael("Ravael","10","RPL")
# person2 = Ravael("Randy","10","RPL")

# print(person1.siswa())
# print(person2.siswa())


#CONTOH DATA SISWA
class Siswa:
    def __init__(self, nis, nama, jurusan, kelas, nilai):
        self.nis = nis
        self.nama = nama
        self.jurusan = jurusan
        self.kelas = kelas
        self.nilai = nilai

    def info(self):
        return (
            f"NIS     : {self.nis}\n"
            f"Nama    : {self.nama}\n"
            f"Kelas   : {self.kelas}\n"
            f"Jurusan : {self.jurusan}\n"
            f"Nilai   : {self.nilai}"
        )

    def status_kelulusan(self):
        if self.nilai >= 75:
            return f"{self.nama} dinyatakan LULUS."
        else:
            return f"{self.nama} dinyatakan TIDAK LULUS."

    def update_kelas(self, kelas_baru):
        self.kelas = kelas_baru
        return f"{self.nama} pindah ke kelas {self.kelas}"

    def update_nilai(self, nilai_baru):
        self.nilai = nilai_baru
        return f"Nilai {self.nama} diupdate menjadi {self.nilai}"
    
Ravael = Siswa("001", "Ravael", "RPL", "10", 80)
Randy = Siswa("002", "Randy", "RPL", "10", 60)

print("===========================")
print(Ravael.info())
print(Ravael.status_kelulusan())

print("=========================")

print(Randy.info())
print(Randy.status_kelulusan())

# Update nilai dan kelas Randy
print("\n--- Update Data Randy ---")
print(Randy.update_nilai(78))
print(Randy.update_kelas("11"))
print(Randy.status_kelulusan())

# Update nilai dan kelas Ravael
print("\n--- Update Data Ravael ---")
print(Ravael.update_nilai(90))
print(Ravael.update_kelas("12"))
print(Ravael.status_kelulusan())
 