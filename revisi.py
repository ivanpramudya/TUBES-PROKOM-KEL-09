import csv
import random
#import sys

#menu awal
def menu():
    print("========================================================================================")
    print("=                        SELAMAT DATANG DI PROGRAM PENCARIAN KOST!                     =")
    print("========================================================================================")
    print("")
menu()

def load_user_data():
    # Load user data from the CSV file
    with open('datauser.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        user_data = list(reader)
    return user_data

def save_user_data(user_data):
    # Save updated user data to the CSV file
    with open('datauser.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(user_data)

def signin():
    print('==============================================================')
    print("")
    print("Sign In")
    username = input("Enter your email or username  : ")
    #username = input("Enter your username      : ")
    password = input("Enter your password           : ")

    user_data = load_user_data()

    for user in user_data:
        if user[0] == username or user[1] == username and user[2] == password:
            print("========================================================================================")
            print("")
            print("                                  INFORMASI PENGGUNA                                    ")
            print("Selamat datang,", user[1])
            return True
    return False


def signup():
    print('==============================================================')
    print("")
    print("Sign Up")
    email = input("Enter your email              : ")
    username = input("Enter a username              : ")
    password = input("Enter a password              : ")

    user_data = load_user_data()

    for user in user_data:
        if user[0] == email or user[1] == username:
            print("Email or username already exists. Please try again.")
            signup()
            break
    
    user_data.append([email,username, password])
    save_user_data(user_data)
    print("Account created successfully. Please sign in.")
    print("")
    signin()

def akun():
    print("Pilih Sign Up jika belum memiliki akun atau pilih Sign In jika sudah memiliki akun.")
    print("1. Sign In")
    print("2. Sign Up")
    choice = input("Choose an option (1/2)        : ")
    if choice == "1":
        if signin():
            print("Login successful!")
            # Call other functions or display menu after successful login
        else:
            print("Invalid username or password.")
            print('==============================================================')
            print("")
            akun()
            # Call login function again or display error message
    elif choice == "2":
        signup()
    else:
        print("Invalid option.")
        print('==============================================================')
        print("")
        akun()
akun()

def buka_detail_data(pilihkost):
    with open('datakost.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i in csv_reader:
            if i[0] == pilihkost:
                print('==============================================================')
                print("")
                print("                         DETAIL KOST                         ")
                print("")
                print(f"Nama Kost                   : {i[1]}")
                print(f"Alamat                      : {i[3]}")
                print(f"Ukuran                      : {i[4]}")
                print(f"Harga Kost/Tahun            : {i[5]}")
                print(f"Fasilitas                   : {i[6]}")
                print(f"Narahubung                  : {i[7]}")
                print(f"Jumlah Kamar yang Tersedia  : {i[8]}")
                print('==============================================================')
                return True
        return False

def aplikasi():
    global total_harga
    with open('datakost.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        print("")
        print("Selamat datang di Program Pencarian Kost!")
        print("Pilih Jenis Kost (L/P)")
        jeniskost = input("Jenis Kost: ")
        daftar_kost = []

        if jeniskost.upper() == 'L':
            print("Berikut Daftar Harga Kost/Tahun:")
            print("1. Kurang dari Rp. 5.000.000")
            print("2. Rp. 5.000.000 sampai Rp. 10.000.000")
            print("3. Lebih dari Rp. 10.000.000")
            harga = input("Pilih Daftar Harga Kost/Tahun (1/2/3) : ")
            if harga == '1':
                print('==============================================================')
                print("")
                print("DAFTAR KOST:")
                for i in csv_reader:
                    if int(i[5]) <= 5000000 and i[2] == 'L':
                        daftar_kost.append(i)
                        print(f'{i[0]}. {i[1]}')
            elif harga == '2':
                print('==============================================================')
                print("")
                print("DAFTAR KOST:")
                for i in csv_reader:
                    if 5000000 < int(i[5]) <= 10000000 and i[2] == 'L':
                        daftar_kost.append(i)
                        print(f'{i[0]}. {i[1]}')
            elif harga == '3':
                print('==============================================================')
                print("")
                print("DAFTAR KOST:")
                for i in csv_reader:
                    if int(i[5]) > 10000000 and i[2] == 'L':
                        daftar_kost.append(i)
                        print(f'{i[0]}. {i[1]}')
            else:
                print("Pilihan tidak valid.")
                print('==============================================================')
                aplikasi()

        elif jeniskost.upper() == 'P':
            print("Berikut Daftar Harga Kost/Tahun:")
            print("1. Kurang dari Rp. 5.000.000")
            print("2. Rp. 5.000.000 sampai Rp. 10.000.000")
            print("3. Lebih dari Rp. 10.000.000")
            harga = input("Pilih Daftar Harga Kost/Tahun (1/2/3) : ")
            if harga == '1':
                print('==============================================================')
                print("")
                print("DAFTAR KOST:")
                for i in csv_reader:
                    if int(i[5]) <= 5000000 and i[2] == 'P':
                        daftar_kost.append(i)
                        print(f'{i[0]}. {i[1]}')
            elif harga == '2':
                print('==============================================================')
                print("")
                print("DAFTAR KOST:")
                for i in csv_reader:
                    if 5000000 < int(i[5]) <= 10000000 and i[2] == 'P':
                        daftar_kost.append(i)
                        print(f'{i[0]}. {i[1]}')
            elif harga == '3':
                print('==============================================================')
                print("")
                print("DAFTAR KOST:")
                for i in csv_reader:
                    if int(i[5]) > 10000000 and i[2] == 'P':
                        daftar_kost.append(i)
                        print(f'{i[0]}. {i[1]}')
            else:
                print("Pilihan tidak valid.")
                print('==============================================================')
                aplikasi()
                
        else:
            print("Pilihan tidak valid.")
            print('==============================================================')
            aplikasi()
        
    print('==============================================================')
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
                if 1 <= jumlahkamar <= int(kost[8]):
                    total_harga = jumlahkamar * int(kost[5])
                    print(f'Total harga sewa: Rp {total_harga}')
                    print("Apakah anda ingin melanjutkan ke menu pembayaran?")
                    print("1. Ya")
                    print("2. Tidak")
                    keputusan = input("Masukkan pilihan (1/2): ")
                        
                    if keputusan == '1':
                        pembayaran()
                    else:
                        print("Silakan kembali ke menu awal")
                        aplikasi()
                else:
                    print("Kamar yang tersedia tidak cukup, akan dikembalikan ke menu awal.")
                    aplikasi()
                #break    
        if not kost_ditemukan:
            print("Detail kos tidak tersedia.")
    elif pilihan == "2":
        aplikasi()
    else:
        print("Pilihan tidak valid.")
        aplikasi()

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
        if total_pembayaran == total_harga:
            kode_bayar = generate_kode_pembayaran()
            print("Kode pembayaran:", kode_bayar)
            kode_input = input("Masukkan kode bayar: ")
            if kode_input == kode_bayar:
                print("Kode pembayaran valid.")
                print("Pembayaran berhasil")
                bukti_pembayaran(pilihan_metode, kode_bayar, total_harga)
            else:
                print("Kode pembayaran tidak valid, silahkan cek kembali kode bayar.")
        else:
            print("Total pembayaran tidak valid, silahkan cek kembali.")

    elif pilihan_metode == "2":
        print("Anda memilih pembayaran dengan BANK BCA :0987654321.")
        total_pembayaran = int(input("Masukkan total pembayaran: "))
        if total_pembayaran == total_harga:
            kode_bayar = generate_kode_pembayaran()
            print("Kode pembayaran:", kode_bayar)
            kode_input = input("Masukkan kode bayar: ")
            if kode_input == kode_bayar:
                print("Kode pembayaran valid.")
                print("Pembayaran berhasil")
                bukti_pembayaran(pilihan_metode, kode_bayar, total_harga)
            else:
                print("Kode pembayaran tidak valid, silahkan cek kembali kode bayar.")
        else:
            print("Total pembayaran tidak valid, silahkan cek kembali.")

    elif pilihan_metode == "3":
        print("Anda memilih pembayaran dengan GOPAY :2222222222.")
        total_pembayaran = int(input("Masukkan total pembayaran: "))
        if total_pembayaran == total_harga:
            kode_bayar = generate_kode_pembayaran()
            print("Kode pembayaran:", kode_bayar)
            kode_input = input("Masukkan kode bayar: ")
            if kode_input == kode_bayar:
                print("Kode pembayaran valid.")
                print("Pembayaran berhasil")
                bukti_pembayaran(pilihan_metode, kode_bayar, total_harga)
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

def bukti_pembayaran(pilihan_metode, kode_bayar, total_harga ):
    print("Bukti Pembayaran:")
    if pilihan_metode == "1":
        metode_pembayaran = "BANK MANDIRI"
    elif pilihan_metode == "2":
        metode_pembayaran = "BANK BCA"
    elif pilihan_metode == "3":
        metode_pembayaran = "GOPAY"
    else:
        metode_pembayaran = "CASH"
    print()
    print('==============================================================')
    print("                         STRUK PEMESANAN                      ")
    print('==============================================================')
    print("                 Metode Pembayaran:", metode_pembayaran)
    print("                 Dengan Kode Bayar:", kode_bayar)
    print("                 Total pembayaran :", total_harga)
    print("          Pemesanan kost sudah otomatis masuk kedalam sistem")
    print("                 Terima kasih atas pembayaran Anda.")

aplikasi()