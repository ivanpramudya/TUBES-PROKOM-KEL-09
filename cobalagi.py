import random

def pembayaran():
    print("Pilih metode pembayaran:")
    print("1. BANK MANDIRI")
    print("2. BANK BCA")
    print("3. GOPAY")
    print("4. CASH")

    pilihan_metode = input("Masukkan nomor metode pembayaran yang dipilih: ")

    if pilihan_metode == "1":
        print("Anda memilih pembayaran dengan BANK MANDIRI : 1234567890 .")
        total_pembayaran = input("Masukkan total pembayaran: ")
        kode_bayar = generate_kode_pembayaran()
        print("Kode pembayaran:", kode_bayar)
        if total_pembayaran == kode_bayar:
            print("Pembayaran berhasil")
            bukti_pembayaran(pilihan_metode, total_pembayaran)
        else:
            print("Total pembayaran tidak valid, silahkan cek kembali.")
            kode_input = input("Masukkan kode bayar: ")
            if kode_input == kode_bayar:
                print("Kode pembayaran valid.")
                bukti_pembayaran(pilihan_metode, total_pembayaran)
            else:
                print("Kode pembayaran tidak valid, silahkan cek kembali kode bayar.")

    elif pilihan_metode == "2":
        print("Anda memilih pembayaran dengan BANK BCA :0987654321.")
        total_pembayaran = input("Masukkan total pembayaran: ")
        kode_bayar = generate_kode_pembayaran()
        print("Kode pembayaran:", kode_bayar)
        if total_pembayaran == kode_bayar:
            print("Pembayaran berhasil")
            bukti_pembayaran(pilihan_metode, total_pembayaran)
        else:
            print("Total pembayaran tidak valid, silahkan cek kembali.")
            kode_input = input("Masukkan kode bayar: ")
            if kode_input == kode_bayar:
                print("Kode pembayaran valid.")
                bukti_pembayaran(pilihan_metode, total_pembayaran)
            else:
                print("Kode pembayaran tidak valid, silahkan cek kembali kode bayar.")

    elif pilihan_metode == "3":
        print("Anda memilih pembayaran dengan GOPAY :2222222222.")
        total_pembayaran = input("Masukkan total pembayaran: ")
        kode_bayar = generate_kode_pembayaran()
        print("Kode pembayaran:", kode_bayar)
        if total_pembayaran == kode_bayar:
            print("Pembayaran berhasil")
            bukti_pembayaran(pilihan_metode, total_pembayaran)
        else:
            print("Total pembayaran tidak valid, silahkan cek kembali.")
            kode_input = input("Masukkan kode bayar: ")
            if kode_input == kode_bayar:
                print("Kode pembayaran valid.")
                bukti_pembayaran(pilihan_metode, total_pembayaran)
            else:
                print("Kode pembayaran tidak valid, silahkan cek kembali kode bayar.")

    elif pilihan_metode == "4":
        print("Silahkan melakukan pembayaran dengan pemilik kost.")

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

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
    print("Metode Pembayaran:", metode_pembayaran)
    print("Total Pembayaran:", total_pembayaran)
    print("Pemesanan kost sudah otomatis masuk kedalam sistem")
    print("Terima kasih atas pembayaran Anda.")

pembayaran()
