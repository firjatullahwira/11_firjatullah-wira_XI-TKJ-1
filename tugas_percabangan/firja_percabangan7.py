#nama: FIRJATULLAH WIRA A
#Kelas: XI TKJ 1
#Absen: 10
#Soal: Sebagai seorang administrator sistem, Anda perlu memutuskan apakah suatu sistem perlu di-restart setelah pembaruan perangkat lunak.

perlu_restart = input("Apakah pembaruan memerlukan restart sistem? (ya/tidak): ")

if perlu_restart.lower() == "ya":
    print("Sistem perlu di-restart.")
else:
    print("Sistem tidak perlu di-restart.")