#nama: FIRJATULLAH WIRA A
#Kelas: XI TKJ 1
#Absen: 10
#Soal: Sebagai seorang analis data, Anda harus mengkategorikan produk berdasarkan penjualan bulanan.

penjualan_bulanan = int(input("Masukkan jumlah penjualan bulanan produk: "))

if penjualan_bulanan > 1000:
    kategori = "Produk Terlaris"
elif penjualan_bulanan >= 500 and penjualan_bulanan <= 1000:
    kategori = "Produk Populer"
else:
    kategori = "Produk Biasa"

print(f"Kategori produk: {kategori}")
