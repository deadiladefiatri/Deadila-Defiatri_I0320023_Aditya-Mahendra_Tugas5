#Menyapa Pengunjung Hotel

NamaPengunjung = str(input("Sebutkan Nama Anda : "))
JenisKelamin = str(input("Masukkan Jenis Kelamin (L/P) : "))

if JenisKelamin == "P" :
    print("Selamat Datang Nyonya", NamaPengunjung)
else :
    print('Selamat Datang Tuan', NamaPengunjung)
