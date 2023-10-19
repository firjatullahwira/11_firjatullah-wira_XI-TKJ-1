def hitung_diskon(total_belanjaan):
    if total_belanjaan > 500000:
        return 0.1  # 10% diskon
    elif 300000 <= total_belanjaan <= 500000:
        return 0.05  # 5% diskon
    else:
        return 0  # Tidak ada diskon

total_belanjaan = float(input("Masukkan total belanjaan: "))
diskon = hitung_diskon(total_belanjaan)

if diskon > 0:
    jumlah_diskon = total_belanjaan * diskon
    total_bayar = total_belanjaan - jumlah_diskon
    print(f"Total belanjaan: Rp {total_belanjaan}")
    print(f"Diskon: Rp {jumlah_diskon}")
    print(f"Total bayar: Rp {total_bayar}")
else:
    print(f"Total belanjaan: Rp {total_belanjaan}")
    print("Tidak ada diskon diberikan.")

# Simpan sebagai berkas 'nama_praktek_1.py'
