import os
os.system('cls')
from prettytable import PrettyTable
x = PrettyTable ()

x.field_names = ["Kode Menu", "Rasa", "Harga"]
x.add_row(["1", "Pepperoni", "40,000"])
x.add_row(["2", "Chiken", "45,000"])
x.add_row(["3","Beef", "60,000"])
x.add_row(["4", "Mushroom", "45,000"])
x.add_row(["5","Cheese", "50,000"])
x.add_row(["6","Tomato", "40,000"])
x.add_row(["7","Mix", "55,000"])


def menu_pembeli():
    print
    print("\nMENU PIZZA:\n")
    print(x)


def pesan_menu_pembeli():
    pesanan = []  
    menu_pembeli()  

    while True:
        nomor_menu = input("\nMasukkan nomor menu yang ingin dipesan (Gunakan kode angka untuk memesan dan ketik 's' apabila selesai memesan): ")
        
        if nomor_menu == "s":
            if len(pesanan) == 0:
                print("Anda belum ")
            else:
                print("\nIni yang anda pesan:\n")
                for pesanan_menu in pesanan:
                    print(pesanan_menu)
                print("\nSilahkan melanjutkan transaksi dengan pegawai kami.")
                exit()
        elif nomor_menu.isnumeric() and 1 <= int(nomor_menu) <= len(x._rows):
            nomor_menu = int(nomor_menu)
            menu = x._rows[nomor_menu - 1][1] 
            pesanan.append(menu)
            print(f"{menu} berhasil ditambahkan ke pesanan Anda.")
        else:
            print("Menu tidak valid. Silakan masukkan nomor menu yang benar.")


def menu_admin():
    while True:
        print("\nSilahkan Memilih Aksi yang ingin dilakukan:")
        print("1. Tampilan menu (read)")
        print("2. Tambahkan Menu (create)")
        print("3. Update Menu (update)")
        print("4. Hapus Menu (delete)")
        print("5. Keluar")

        pilihan = input("Pilih tindakan (1/2/3/4/5): ")

        if pilihan == "1":
            print(x)
        elif pilihan == "2":
            nomor = input("Masukkan nomor menu baru (harap melanjutkan angka sesuai menu): ")
            rasa = input("Masukkan nama menu baru: ")
            harga = input("Masukkan harga menu: ")
            x.add_row([nomor, rasa, harga])
            print("Menu berhasil ditambahkan.")
        elif pilihan == "3":
            kode_menu = input("Masukkan nomor menu yang ingin diedit: ")
            indeks = x.field_names.index("Kode Menu")
            for row in x._rows:
                if row[indeks] == kode_menu:
                    rasa = input("Masukkan nama menu baru: ")
                    harga = input("Masukkan harga menu baru: ")
                    row[1] = rasa
                    row[2] = harga
                    print("Menu berhasil diedit.")
                    break
            else:
                print("Menu tidak ditemukan.")
        elif pilihan == "4":
            kode_menu = input("Masukkan nomor menu yang ingin dihapus: ")
            indeks = x.field_names.index("Kode Menu")
            new_rows = []
            for row in x._rows:
                if row[indeks] != kode_menu:
                    new_rows.append(row)
            x._rows = new_rows
            print("Menu berhasil dihapus.")
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def tampilan_awal():
    while True:
        print("==================================")
        print("Selamat datang di Farhan Pizzaria!")
        print("==================================")
        print("1. Pembeli")
        print("2. Admin")
        print("3. Keluar toko")
        role = input("Disini anda sebagai? (1/2/3): ")

        if role == "1":
            print("==================================")
            print("Selamat datang di Farhan Pizzaria!")
            print("==================================")
            pesan_menu_pembeli()
        elif role == "2":
            print("=============================")
            print("Selamat datang di menu admin")
            print("============================")
            menu_admin()
        elif role == "3":
            print("Terimakasih atas kunjungannya...")
            break
        else:
            print("Role tidak valid, Silakan coba lagi.")

if __name__ == "__main__":
    tampilan_awal()













