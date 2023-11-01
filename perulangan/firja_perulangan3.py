#nama: Firjatullah wira a
#Kelas: XI TKJ 1
#Absen: 10
#Deskripsi Pekerjaan: Sebuah investasi awal sebesar 10.000 dollar tumbuh sebesar 6% setiap tahunnya. Buatlah program yang menghitung berapa tahun yang dibutuhkan agar nilai investasi melebihi 20.000 dollar.Rumus: Nilai investasi tahun ke-n = Nilai investasi tahun ke-(n-1) + 6% dari Nilai investasi tahun ke-(n-1)

investasi_awal = 10000  # Nilai investasi awal
tingkat_pertumbuhan = 0.06  # Tingkat pertumbuhan (6%)
nilai_investasi = investasi_awal
tahun = 0

# Mulai menghitung hingga nilai investasi melebihi $20,000
while nilai_investasi <= 20000:
    tahun += 1
    nilai_investasi += nilai_investasi * tingkat_pertumbuhan

print(f'Dibutuhkan {tahun} tahun agar nilai investasi melebihi $20,000.')
