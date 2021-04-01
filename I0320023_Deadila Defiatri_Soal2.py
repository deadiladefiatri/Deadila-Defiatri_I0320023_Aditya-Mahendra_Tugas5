#Grading Nilai

Nama = str(input('Nama Lengkap : '))
Nilai = int(input('Nilai Anda skala 1-100: '))

info = 'Halo ' + Nama + '!' + ' Nilai anda setelah dikonversi adalah '

#memeriksa nilai
if Nilai <= 100 and Nilai >= 85:
    print(info + 'A')
elif Nilai <= 84 and Nilai >= 80:
    print(info + 'A-')
elif Nilai <=79 and Nilai >= 75:
    print(info + 'B+')
elif Nilai <= 74 and Nilai >= 70:
    print(info + 'B')
elif Nilai <=69 and Nilai >= 65:
    print(info + 'C+')
elif Nilai <= 64 and Nilai >= 60:
    print(info + 'C')
elif Nilai <=59 and Nilai >= 0:
    print(info + 'E')
else:
    print('Halo' + '' +  Nama + '!' + 'Nilai kamu tidak dapat dikonversi')



