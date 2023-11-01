#nama: Firjatullah wira a
#kelas: XI TKJ 1
#Absen: 10
#Di sebuah toko online, Anda bertanggung jawab untuk menghitung diskon berdasarkan jumlah total belanjaan pelanggan.

total_belanjaan = float(input("Masukkan total belanjaan: "))

if total_belanjaan > 500000:
    diskon = 0.10  # Diskon 10%
    total_belanjaan -= total_belanjaan * diskon
    print(f"Total belanjaan setelah diskon: {total_belanjaan:.2f} dollar")
elif total_belanjaan >= 300000 and total_belanjaan <= 500000:
    diskon = 0.05  # Diskon 5%
    total_belanjaan -= total_belanjaan * diskon
    print(f"Total belanjaan setelah diskon: {total_belanjaan:.2f} dollar")
else:
    print(f"Total belanjaan: {total_belanjaan:.2f} dollar (Tidak ada diskon)")
