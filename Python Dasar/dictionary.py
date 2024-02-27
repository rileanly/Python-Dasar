nilai_IPA = { "Joni" = 7, 
             "Yolgi" = 8, 
             "Jonathan" = 8, 
             "Hizkia"= 7, 
             "Marlon" = 8}
nama = input("Masukkan nama siswa :")
if nama in nilai_IPA:
    print("Nilai IPA ", nama, "adalah", nilai_IPA[nama])
else:
    print("data siswa tidak ditemukan")
    print("berikut nama-nama siswa")
    for i in nilai_IPA.keys():
        print(i)











