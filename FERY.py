import csv

def buka_detail_data(pilihkost):
    with open('datakost.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i in csv_reader:
            if i[0] == pilihkost:
                print(f"Nama Kost: {i[1]}, Jenis Kost: {i[2]}, Alamat: {i[3]}, Ukuran: {i[4]}, Fasilitas: {i[6]}, Narahubung: {i[7]}")
                return True
        return False


def main():
    print("Selamat datang di Aplikasi Daftar Kost!")
    print("Pilih Jenis Kost (L/P)")
    jeniskost = input("Jenis Kost: ")
    print("Berikut Daftar Harga Kost/Tahun:")
    print("1. Kurang dari Rp. 5.000.000")
    print("2. Rp. 5.000.000 sampai Rp. 10.000.000")
    print("3. Lebih dari Rp. 10.000.000")
    harga = input("Pilih Daftar Harga Kost/Tahun (1/2/3) : ")

    with open('datakost.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        daftar_kost = []

        if jeniskost == 'L':
            print("DAFTAR KOST:")
            if harga == '1':
                for i in csv_reader:
                    if int(i[5]) <= 5000000 and i[2] == 'L':
                        daftar_kost.append(i)
                        print(f'{i[0]}. {i[1]}')
            elif harga == '2':
                for i in csv_reader:
                    if 5000000 < int(i[5]) <= 10000000 and i[2] == 'L':
                        daftar_kost.append(i)
                        print(f'{i[0]}. {i[1]}')
            else:
                for i in csv_reader:
                    if int(i[5]) > 10000000 and i[2] == 'L':
                        daftar_kost.append(i)
                        print(f'{i[0]}. {i[1]}')

        elif jeniskost == 'P':
            print("DAFTAR KOST:")
            if harga == '1':
                for i in csv_reader:
                    if int(i[5]) <= 5000000 and i[2] == 'P':
                        daftar_kost.append(i)
                        print(f'{i[0]}. {i[1]}')
            elif harga == '2':
                for i in csv_reader:
                    if 5000000 < int(i[5]) <= 10000000 and i[2] == 'P':
                        daftar_kost.append(i)
                        print(f'{i[0]}. {i[1]}')
            else:
                for i in csv_reader:
                    if int(i[5]) > 10000000 and i[2] == 'P':
                        daftar_kost.append(i)
                        print(f'{i[0]}. {i[1]}')

    print("Apakah Anda ingin membuka detail salah satu kost?")
    print("1. Ya")
    print("2. Tidak")
    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan == "1":
        pilihkost = input("Pilih nomor kost pada daftar untuk melihat detail: ")
        kost_ditemukan = False
        for kost in daftar_kost:
            if kost[0] == pilihkost:
                buka_detail_data(pilihkost)
                kost_ditemukan = True
                break
        if not kost_ditemukan:
            print("Detail kos tidak tersedia.")
    elif pilihan == "2":
        print("Tidak membuka detail kost.")

    else:
        print("Pilihan tidak valid.")

if __name__== "__main__":
    main()