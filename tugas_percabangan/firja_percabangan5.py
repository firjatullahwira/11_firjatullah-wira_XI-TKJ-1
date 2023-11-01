#nama: FIRJATULLAH WIRA A
#Kelas: XI TKJ 1
#Absen: 10
#Soal: Sebagai seorang guru, Anda harus menentukan nilai akhir siswa berdasarkan nilai tugas dan ujian.

nilai_tugas = float(input("Masukkan nilai tugas (skala 0-100): "))
nilai_ujian = float(input("Masukkan nilai ujian (skala 0-100): "))

if nilai_tugas > 70 and nilai_ujian > 60:
    nilai_akhir = "Lulus"
else:
    nilai_akhir = "Gagal"

print(f"Hasil: {nilai_akhir}")