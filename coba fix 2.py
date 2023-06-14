import csv
import random

print("SELAMAT DATANG GUISSSS!")
print("MAU CARI KOS YA???!")
print("LOGIN DULU YA BESTIII, KALAU BELUM PUNYA AKUN SIGN UP DULS OKE")

def load_user_data():
    # Load user data from the CSV file
    with open('datauser.csv', 'r') as file:
        reader = csv.reader(file)
        user_data = list(reader)
    return user_data

def save_user_data(user_data):
    # Save updated user data to the CSV file
    with open('datauser.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(user_data)

def login():
    email = input ("enter your email     :")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    user_data = load_user_data()

    for user in user_data:
        if user[0] == email and user == username [1] and user[2] == password:
            return True

    return False

def signup():
    email = input ("enter your email:")
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    user_data = load_user_data()

    for user in user_data:
        if user[0] == username:
            print("Username already exists. Please try again.")
            return

    user_data.append([email,username, password])
    save_user_data(user_data)
    print("Account created successfully. Please sign in.")

# Menu
print("Welcome!")
print("1. Sign In")
print("2. Sign Up")

choice = input("Choose an option: ")

if choice == "1":
    if login():
        print("Login successful!")
        # Call other functions or display menu after successful login
    else:
        print("Invalid username or password.")
        # Call login function again or display error message
elif choice == "2":
    signup()
else:
    print("Invalid option.")

def datauser():
    global nama

    print('                 INFORMASI PENGGUNA')
    nama = input('Masukkan username anda :')
    for i in nama:
        if i.isdigit():
            print("Tolong Masukan Dengan Huruf")
            datauser()
    print()
    print('======================================================')
    print()
    print(                " Selamat Datang", nama, "!")
    print(                " Silakan pilih kos yang lo mau deh", nama, "!")
datauser()

def buka_detail_data(pilihkost):
    with open('datakost.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i in csv_reader:
            if i[0] == pilihkost:
                print(f"Nama Kost: {i[1]}, Jenis Kost: {i[2]}, Alamat: {i[3]}, Ukuran: {i[4]}, Harga Kost/Tahun: {i[5]}, Fasilitas: {i[6]}, Narahubung: {i[7]}, Jumlah Kamar yang Tersedia: {i[8]}")
                return True
        return False


def main():
    while True:
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
                    jumlahkamar = int(input("Masukkan jumlah kamar kost yang ingin disewa: "))
                    if jumlahkamar <= int(kost[8]):
                        print("Apakah anda ingin melanjutkan ke menu pembayaran?")
                        print("1. Ya")
                        print("2. Tidak")
                        keputusan = input("Masukkan pilihan (1/2): ")
                        
                        if keputusan == '1':
                            total_harga = jumlahkamar * int(kost[5])
                            print(f'Total harga sewa: Rp {total_harga}')
                        else:
                            print("Silakan kembali ke menu awal")
                    else:
                        print("Kamar yang Tersedia tidak cukup")
                    #break    
            if not kost_ditemukan:
                print("Detail kos tidak tersedia.")
        elif pilihan == "2":
            print("Tidak membuka detail kost.")
        else:
            print("Pilihan tidak valid.")
        
        kembali_ke_menu = input("Apakah Anda ingin kembali ke menu awal? (Y/N): ")
        if kembali_ke_menu.lower() != "y":
            break

        print()

if __name__== "__main__":
    main()

import random

def validate_payment():
    def generate_kode_pembayaran():
        kode_bayar = ''.join(random.choices('0123456789', k=6))
        return kode_bayar

    def bukti_pembayaran(pilihan_metode, total_pembayaran, kode_bayar):
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
        print("                         STRUK PEMESANAN                    ")
        print('==============================================================')
        print("                 Metode Pembayaran:", metode_pembayaran)
        print("                 Total Pembayaran :", total_pembayaran)
        print("                 Dengan Kode Bayar:", kode_bayar)
        print("          Pemesanan kost sudah otomatis masuk kedalam sistem")
        print("                 Terima kasih atas pembayaran Anda.")

    print("Pilih metode pembayaran:")
    print("1. BANK MANDIRI")
    print("2. BANK BCA")
    print("3. GOPAY")
    print("4. CASH")

    pilihan_metode = input("Masukkan nomor metode pembayaran yang dipilih: ")

    if pilihan_metode in ["1", "2", "3"]:
        if pilihan_metode == "1":
            print("Anda memilih pembayaran dengan BANK MANDIRI : 1234567890 .")
        elif pilihan_metode == "2":
            print("Anda memilih pembayaran dengan BANK BCA : 0987654321.")
        elif pilihan_metode == "3":
            print("Anda memilih pembayaran dengan GOPAY : 2222222222.")

        total_pembayaran = input("Masukkan total pembayaran: ")
        kode_bayar = generate_kode_pembayaran()
        print("Kode pembayaran:", kode_bayar)

        if total_pembayaran == kode_bayar:
            print("Pembayaran berhasil")
            bukti_pembayaran(pilihan_metode, total_pembayaran, kode_bayar)
        else:
            print("Total pembayaran tidak valid, silahkan cek kembali.")
            kode_input = input("Masukkan kode bayar: ")
            if kode_input == kode_bayar:
                print("Kode pembayaran valid.")
                bukti_pembayaran(pilihan_metode, total_pembayaran, kode_bayar)
            else:
                print("Kode pembayaran tidak valid, silahkan cek kembali kode bayar.")

    elif pilihan_metode == "4":
        print("Silahkan melakukan pembayaran dengan pemilik kost.")

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

    validate_payment()

validate_payment()
