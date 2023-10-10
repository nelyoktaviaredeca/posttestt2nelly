dictionary = {'bunga': ['Bunga Mawar', 'Bunga Matahari', 'Bunga Camelia', 'Bunga PomPom', 'Bunga Gerbera'],
              'harga': [20000, 35000, 20000, 15000, 25000]}
transaksi_pembeli = []


def tambah():
    jenis_bunga = input("Masukkan jenis bunga baru: ")
    if jenis_bunga not in dictionary['bunga']:
        harga_bunga = int(input("Masukkan harga bunga baru: "))
        dictionary['bunga'].append(jenis_bunga)
        dictionary['harga'].append(harga_bunga)
        print(f"{jenis_bunga} berhasil ditambahkan.")
    else:
        print(f"{jenis_bunga} sudah ada dalam daftar.")


def lihat(dictionary):
    print("|-----------------------------------------|")
    print("|        Daftar Jenis Bunga               |")
    print("|-----------------------------------------|")
    for i, jenis in enumerate(dictionary['bunga']):
        print(f"|{i + 1}. {jenis} - Harga: {dictionary['harga'][i]}|")
    print("|-----------------------------------------|")


def perbarui():
    lihat(dictionary)
    index = int(input("Masukkan nomor jenis bunga yang ingin diperbarui: ")) - 1
    if 0 <= index < len(dictionary['bunga']):
        jenis_baru = input("Masukkan jenis bunga baru: ")
        harga_baru = int(input("Masukkan harga bunga baru: "))
        dictionary['bunga'][index] = jenis_baru
        dictionary['harga'][index] = harga_baru
        print(f"Jenis bunga #{index + 1} berhasil diperbarui.")
    else:
        print("Nomor jenis bunga tidak valid.")


def hapus():
    lihat(dictionary)
    index = int(input("Masukkan nomor jenis bunga yang ingin dihapus: ")) - 1
    if 0 <= index < len(dictionary['bunga']):
        jenis_hapus = dictionary['bunga'].pop(index)
        harga_hapus = dictionary['harga'].pop(index)
        print(f"{jenis_hapus} - Harga: {harga_hapus} berhasil dihapus.")
    else:
        print("Nomor jenis bunga tidak valid.")


def transaksi_pembeli_pilihan():
    lihat(dictionary)
    index = int(input("Masukkan nomor jenis bunga yang ingin dibeli: ")) - 1
    if 0 <= index < len(dictionary['bunga']):
        jumlah = int(input("Masukkan jumlah bunga yang ingin dibeli: "))
        total_harga = jumlah * dictionary['harga'][index]
        print(f"Total harga untuk {jumlah} {dictionary['bunga'][index]} adalah: {total_harga}")
        transaksi_pembeli.append((dictionary['bunga'][index], jumlah, total_harga))
    else:
        print("Nomor jenis bunga tidak valid.")


def start():
    while True:
        print("|-----------------------------------------|")
        print("|       Blossom Artistry Boutique         |")
        print("|-----------------------------------------|")
        print("| 1. ADMIN                                |")
        print("| 2. PEMBELI                              |")
        print("|-----------------------------------------|")
        pilihan = int(input("Masukkan pilihan : "))

        if pilihan == 1:
            print("|-----------------------------------------|")
            print("|       Blossom Artistry Boutique         |")
            print("|-----------------------------------------|")
            print("| 1. MENAMBAHKAN JENIS BUNGA              |")
            print("| 2. MELIHAT JENIS BUNGA                  |")
            print("| 3. MEMPERBARUI JENIS BUNGA              |")
            print("| 4. MENGHAPUS JENIS BUNGA                |")
            print("|-----------------------------------------|")

            pilih = int(input("Masukkan pilihan : "))
            if pilih == 1:
                tambah()
            elif pilih == 2:
                lihat(dictionary)
            elif pilih == 3:
                perbarui()
            elif pilih == 4:
                hapus()
            else:
                print("Pilihan tidak valid.")
        elif pilihan == 2:
            print("|-----------------------------------------|")
            print("|       Blossom Artistry Boutique         |")
            print("|-----------------------------------------|")
            print("| PEMBELI                                |")
            print("| 1. TRANSAKSI PEMBELIAN                  |")
            print("|-----------------------------------------|")

            pilih = int(input("Masukkan pilihan : "))
            if pilih == 1:
                transaksi_pembeli_pilihan()
            else:
                print("Pilihan tidak valid.")
        else:
            print("Pilihan tidak valid.")

start()