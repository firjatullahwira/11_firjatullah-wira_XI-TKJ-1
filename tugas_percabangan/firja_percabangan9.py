#nama: Firjatullah wira a
#Kelas: XI TKJ 1
#Absen: 10
#soal : sebagai seorang pelajar pustakawan, anda perlu menentukan jenis pinjaman buku berdasarkan durasi peminjaman

durasi_peminjaman = int(input("Masukkan durasi peminjaman buku dalam hari: "))

if durasi_peminjaman <= 7:
    jenis_pinjaman = "Peminjaman Pendek"
elif durasi_peminjaman > 7 and durasi_peminjaman <= 30:
    jenis_pinjaman = "Peminjaman Menengah"
else:
    jenis_pinjaman = "Peminjaman Panjang"

print(f"Jenis pinjaman: {jenis_pinjaman}")
