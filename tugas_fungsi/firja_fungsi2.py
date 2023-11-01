#nama: Firjatullah wira a
#Kelas: XI TKJ 1
#Absen: 10
#Soal: Buatlah sebuah fungsi untuk menghitung faktorial dari suatu bilangan.

def hitung_faktorial(n):
    if n < 0:
        return "Faktorial tidak terdefinisi untuk bilangan negatif"
    elif n == 0:
        return 1
    else:
        faktorial = 1
        for i in range(1, n + 1):
            faktorial *= i
        return faktorial
bilangan = 5
hasil = hitung_faktorial(bilangan)
print(f"Faktorial dari {bilangan} adalah {hasil}")