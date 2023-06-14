import random
import csv

def buka_detail_data(pilihkost):
    with open('datakost.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i in csv_reader:
            if i[0] == pilihkost:
                print("=========================================================")
                print("")
                print("                       DETAIL KOST                       ")
                print("")
                print(f"Nama Kost                   : {i[1]}")
                print(f"Alamat                      : {i[3]}")
                print(f"Ukuran                      : {i[4]}")
                print(f"Harga Kost/Tahun            : {i[5]}")
                print(f"Fasilitas                   : {i[6]}")
                print(f"Narahubung                  : {i[7]}")
                print(f"Jumlah Kamar yang Tersedia  : {i[8]}")
                print("=========================================================")
                return True
        return False

def aplikasi():
    with open('datakost.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        #print("==========================================")
        print("")
        print("Pilih Jenis Kost (L/P)")
        jeniskost = input("Jenis Kost: ")
        daftar_kost = []

        if jeniskost.upper() == 'L':
            print("Berikut Daftar Harga Kost/Tahun:")
            print("1. Kurang dari Rp. 5.000.000")
            print("2. Rp. 5.000.000 sampai Rp. 10.000.000")
            print("3. Lebih dari Rp. 10.000.000")
            harga = input("Pilih Daftar Harga Kost/Tahun (1/2/3) : ")
            print("==========================================")
            print("")
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
            elif harga == '3':
                for i in csv_reader:
                    if int(i[5]) > 10000000 and i[2] == 'L':
                        daftar_kost.append(i)
                        print(f'{i[0]}. {i[1]}')
            else:
                print("Pilihan tidak valid.")
                print("==========================================")
                aplikasi()

        elif jeniskost.upper() == 'P':
            print("Berikut Daftar Harga Kost/Tahun:")
            print("1. Kurang dari Rp. 5.000.000")
            print("2. Rp. 5.000.000 sampai Rp. 10.000.000")
            print("3. Lebih dari Rp. 10.000.000")
            harga = input("Pilih Daftar Harga Kost/Tahun (1/2/3) : ")
            print("==========================================")
            print("")
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
            elif harga == '3':
                for i in csv_reader:
                    if int(i[5]) > 10000000 and i[2] == 'P':
                        daftar_kost.append(i)
                        print(f'{i[0]}. {i[1]}')
            else:
                print("Pilihan tidak valid.")
                print("==========================================")
                aplikasi()

        else:
            print("Pilihan tidak valid.")
            print("==========================================")
            aplikasi()
    print("")
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
                print("")
                jumlahkamar = int(input("Masukkan jumlah kamar kost yang ingin disewa: "))
                if jumlahkamar <= int(kost[8]):
                    total_harga = jumlahkamar*int(kost[5])
                    print(f'Total harga sewa: Rp {total_harga}')
                    print("Apakah anda ingin melanjutkan ke menu pembayaran?")
                    print("1. Ya")
                    print("2. Tidak")
                    keputusan = input("Masukkan pilihan (1/2): ")
                        
                    if keputusan == '1':
                        pembayaran()
                    elif keputusan == '2':
                        print("Silakan kembali ke menu awal")
                    else:
                        print("Pilihan tidak valid.")
                else:
                    print("Kamar yang Tersedia tidak cukup")
                
                kembali_ke_menu = input("Apakah Anda ingin kembali ke menu awal? (Y/N): ")
                if kembali_ke_menu.lower() != "y":
                    break   
                print()
        if not kost_ditemukan:
            print("Detail kos tidak tersedia.")
    elif pilihan == "2":
        print("==========================================")
        aplikasi()
    else:
        print("Pilihan tidak valid.")
        print("==========================================")

def pembayaran():
    print("")
    print("Pilih metode pembayaran:")
    print("1. BANK MANDIRI")
    print("2. BANK BCA")
    print("3. GOPAY")
    print("4. CASH")

    pilihan_metode = input("Masukkan nomor metode pembayaran yang dipilih: ")

    if pilihan_metode == "1":
        print("Anda memilih pembayaran dengan BANK MANDIRI : 1234567890 .")
        total_pembayaran = int(input("Masukkan total pembayaran: "))
        if total_pembayaran == int(kost[8]):
            kode_bayar = generate_kode_pembayaran()
            print("Kode pembayaran:", kode_bayar)
            print("Pembayaran berhasil")
            kode_input = input("Masukkan kode bayar: ")
            if kode_input == kode_bayar:
                print("Kode pembayaran valid.")
                bukti_pembayaran(pilihan_metode, total_pembayaran)
            else:
                print("Kode pembayaran tidak valid, silahkan cek kembali kode bayar.")
        else:
            print("Total pembayaran tidak valid, silahkan cek kembali.")

    elif pilihan_metode == "2":
        print("Anda memilih pembayaran dengan BANK BCA :0987654321.")
        total_pembayaran = int(input("Masukkan total pembayaran: "))
        if total_pembayaran == kode_bayar:
            kode_bayar = generate_kode_pembayaran()
            print("Kode pembayaran:", kode_bayar)
            print("Pembayaran berhasil")
            kode_input = input("Masukkan kode bayar: ")
            if kode_input == kode_bayar:
                print("Kode pembayaran valid.")
                bukti_pembayaran(pilihan_metode, total_pembayaran)
            else:
                print("Kode pembayaran tidak valid, silahkan cek kembali kode bayar.")
        else:
            print("Total pembayaran tidak valid, silahkan cek kembali.")

    elif pilihan_metode == "3":
        print("Anda memilih pembayaran dengan GOPAY :2222222222.")
        total_pembayaran = int(input("Masukkan total pembayaran: "))
        if total_pembayaran == kode_bayar:
            kode_bayar = generate_kode_pembayaran()
            print("Kode pembayaran:", kode_bayar)
            print("Pembayaran berhasil")
            kode_input = input("Masukkan kode bayar: ")
            if kode_input == kode_bayar:
                print("Kode pembayaran valid.")
                bukti_pembayaran(pilihan_metode, total_pembayaran)
            else:
                print("Kode pembayaran tidak valid, silahkan cek kembali kode bayar.")
        else:
            print("Total pembayaran tidak valid, silahkan cek kembali.")

    elif pilihan_metode == "4":
        print("Silahkan melakukan pembayaran dengan pemilik kost.")

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        pembayaran()

def generate_kode_pembayaran():
    kode_bayar = ''.join(random.choices('0123456789', k=6))
    return kode_bayar

def bukti_pembayaran(pilihan_metode, total_pembayaran):
    print("Bukti Pembayaran:")
    print("Nomor Invoice: INV123456789")
    if pilihan_metode == "1":
        metode_pembayaran = "BANK MANDIRI"
    elif pilihan_metode == "2":
        metode_pembayaran = "BANK BCA"
    elif pilihan_metode == "3":
        metode_pembayaran = "GOPAY"
    else:
        metode_pembayaran = "CASH"
    print(f"Metode Pembayaran: {metode_pembayaran}")
    print(f"Total Pembayaran: {total_pembayaran}")

aplikasi()
