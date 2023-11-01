#nama: Firjatullah wira a
#Kelas: XI TKJ 1
#Absen: 10
#Sebagai seorang manajer proyek, Anda harus menentukan apakah suatu proyek akan selesai tepat waktu atau terlambat.

estimasi_waktu_selesai = input("Masukkan estimasi waktu selesai (format: YYYY-MM-DD): ")
tanggal_target_selesai = input("Masukkan tanggal target selesai (format: YYYY-MM-DD): ")

if estimasi_waktu_selesai <= tanggal_target_selesai:
    print("Tepat waktu")
else:
    print("Terlambat")
