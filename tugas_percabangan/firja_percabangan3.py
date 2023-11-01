#nama: Firjatullah wira a
#Kelas: XI TKJ 1
#Absen: 10
#Soal: Sebagai seorang sistem administrator, Anda bertanggung jawab untuk memeriksa apakah suatu file di server sudah ada atau belum sebelum menggantinya.

import os
direktori = '/path/to/direktori/server'
nama_file = 'nama_file_yang_dicari.txt'

path_file = os.path.join(direktori, nama_file)

if os.path.exists(path_file):
    print("File sudah ada.")
else:
    print("File belum ada.")
