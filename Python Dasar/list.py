# menu_item = 0
# namelist = []

# while menu_item != 9:
#     print("1. Tampilkan nama dalam list :")
#     print("2. Tambahkan nama dalam list :")
#     print("3. Ubah nama dalam list :")
#     print("4. Hapus nama dalam list :")
#     print("9. keluar")

#     menu_item = int(input("Pilih menu item :"))
#     if menu_item == 1:
#         current = 0
#         if len(namelist) > 0:
#             while current < len(namelist):
#                 print(current, ".", namelist[current])
#                 current += 1
#         else:
#             print("Nama dalam list kosong")
#     elif menu_item == 2:
#         tambah_nama = input("Masukkan nama yang ingin ditambahkan :")
#         namelist.append(tambah_nama)
#         print("Nama ", tambah_nama,  "telah berhasil ditambahkan")
#     elif menu_item == 3:
#         old_name = input("Nama yang ingin diubah :")
#         if old_name in namelist:
#             nama_baru = input("Masukkan nama baru :")
#             item_number = namelist.index(old_name)
#             namelist[item_number] = nama_baru
#             print("Nama ", old_name, "telah berhasil diubah")
#         else:
#             print("Nama tidak ada di dalam list")
#     elif menu_item == 4:
#         del_name = input("Masukkan nama yang ingin dihapus :")
#         if del_name in namelist:
#             namelist.remove(del_name)#cara yang di gunakan remove 
#             # item_number = namelist.index(del_name)
#             # del namelist[item_number]
#         else:
#             print(del_name, "Nama tidak ada di dalam list")
#     else:
#         print("Selamat tinggal")

list2 = []
print("isi list 2 adalah :", len(list2))
list2.append("joni")
print("Sekarang list 2 ada :", len(list2))
print("Yaitu: ", list2[0])

list2.insert(0, "Yolgi")#ini untuk mengisi list yang sesuai dengan index yang akan dimasukkan 
print("ini anggota-anggota di list, yaitu :", list2)

list3 = list2.copy()
print("Isi list 3, yaitu :", list3)

list2.extend(list3)
print("Gabungan List 2 dan List 3 ada :", list2)

list2.pop() #untuk menghapus item list terakhir dalam list
print(list2)

list3.clear()#untuk menghapus semua item yang ada di list 3
print(list3)

warna = ["Merah", "Kuning", "Hijau", "Biru" ]
print(*warna, sep = "\n") #Jika menggunakan sep maka kita bisa mengatur isi list sesuai dengan keinginan kita

for item in warna:
    print(item, sep = '\n')

for item in warna:
    print(item.rjust(8), sep = '\n')






