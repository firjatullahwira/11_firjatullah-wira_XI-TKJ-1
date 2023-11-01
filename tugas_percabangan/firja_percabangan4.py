#nama: Firjatullah wira a
#Kelas: XI TKJ 1
#Absen: 10
#soal : Sebagai seorang kasir di toko, Anda harus menghitung jumlah diskon berdasarkan total belanjaan pelanggan dan jenis anggota (anggota biasa atau anggota premium).

total_belanjaan = float(input("Masukkan total belanjaan: "))
status_anggota = input("Masukkan status anggota (premium/biasa): ")

if status_anggota.lower() == "premium":
    if total_belanjaan > 500000:
        diskon = 0.15 
    else:
        diskon = 0.10 
elif status_anggota.lower() == "biasa":
    if total_belanjaan > 300000:
        diskon = 0.07 
    else:
        diskon = 0.00  
else:
    print("Status anggota tidak valid.")
    exit()

total_belanjaan_setelah_diskon = total_belanjaan - (total_belanjaan * diskon)
print(f"Total belanjaan setelah diskon: {total_belanjaan_setelah_diskon:.2f} dollar")
