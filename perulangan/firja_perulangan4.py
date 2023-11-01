#nama: Firjatullah wira a
#kelas: XI TKJ 1
#Absen: 10
#Deskripsi Pekerjaan: Seorang pedagang memiliki 100 buah apel. Setiap harinya, ia menjual 10% dari jumlah apel yang tersisa. Buatlah program yang menghitung berapa hari yang dibutuhkan agar sisa apel kurang dari 20 buah. Rumus: Sisa apel hari ke-n = Sisa apel hari ke-(n-1) - 10% dari Sisa apel hari ke-(n-1)

jumlah_apel = 100  # Jumlah apel awal
hari = 0  # Jumlah hari awal

# Mulai menghitung hingga sisa apel kurang dari 20
while jumlah_apel >= 20:
    hari += 1
    jumlah_apel = jumlah_apel - (0.10 * jumlah_apel)  # Mengurangi 10% dari apel yang tersisa

print(f'Dibutuhkan {hari} hari agar sisa apel kurang dari 20 buah.')
