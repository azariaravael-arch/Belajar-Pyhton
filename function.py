def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("========================")
        print(F"Nama : {kontak['nama']}")
        print(F"Email : {kontak['email']}")
        print(F"Telepon : {kontak['telepon']}")
        
# tambah kontak
def new_kontak():
    Nama = input("nama : ")
    Email = input("email : ")
    Telepon = input("telepon : ")
    kontak = {
        "nama": Nama,
        "email": Email,
        "telepon": Telepon
    }
    return kontak

# hapus kontak
def hapus_kontak(daftar_kontak):
    Telepon = input("No telepon yang akan di hapus: ")
    index = -1
    
    for i in range(0,len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if Telepon == kontak["Telepon"]:
            index = i
            break
    if index == -1:
        print("Data kontak tidak di temukan")
    else:
        del daftar_kontak[index]
        print("Berhasil menghapus data kontak")

# cari kontak
def cari_kontak(daftar_kontak):
    nama_yang_dicari = input("nama yang di cari : ") 
    
    for kontak in daftar_kontak:
        Nama = kontak["nama"]
        
        if Nama.lower().find(nama_yang_dicari.lower()) != -1:
            print(f"Nama: {kontak['nama']}")
            print(f"Email: {kontak['email']}")
            print(f"Telepon: {kontak['telepon']}")
            