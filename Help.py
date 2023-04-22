from login import login, logout, ambil_status_login

def list_help():
    global username, password, login_status, username_status, password_status
    if not ambil_status_login:
        print("=========== HELP ===========")
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
        notlog = input('input: ')
        if notlog == '1':
            login()
        elif notlog == '2':
            instruction()
    else:
        if username == "Bondowoso":
            print("=========== HELP ===========")
            print("1. logout")
            print("   Untuk keluar dari akun yang digunakan sekarang")
            print("2. summon jin")
            print("   Untuk memanggil jin dari alam gaib")
            print("3. Hilangkan jin ")
            print("   untuk menghapus jin dari alam gaib")
            print("4. Ubah Jin")
            print("   Mengubah tipe jin yang telah disummon dari alam gaib")
            opsib = input('input: ')
            if opsib == '1':
                logout()
            elif opsib == '2':
                summon_jin()
            elif opsib == '3':
                hilangkan_jin()
            elif opsib == '4':
                ubah_jin()
        elif username == "Roro":
            print("=========== HELP ===========")
            print("1. logout")
            print("   Untuk keluar dari akun yang digunakan sekarang")
            print("2. Hancurkan candi")
            print("   Untuk menghancurkan candi yang tersedia")
            print("3. Aktifkan Ayam berkokok")
            print("   Roro mempunyai kemampuan untuk memalsukan pagi hari ")
            opsir = input('input: ')
            if opsir == '1':
                logout()
            elif opsir == '2':
                hancurkan_candi()
            elif opsir == '3':
                ayam_berkokok()
        elif username == "Jin Pengumpul":
            print("=========== HELP ===========")
            print("1. logout")
            print("   Untuk keluar dari akun yang digunakan sekarang")
            print("2. kumpul")
            print("   Untuk mengumpulkan resource candi")
            opsijpl = input('input: ')
            if opsijpl == '1':
                logout()
            elif opsijpl == '2':
                kumpul()
        elif username == "Jin Pembangun":
            print("=========== HELP ===========")
            print("1. logout")
            print("   Untuk keluar dari akun yang digunakan sekarang")
            print("2. bangun")
            print("   Untuk membangun candi")
            opsijpn = input('input: ')
            if opsijpn == '1':
                logout()
            elif opsijpn == '2':
                bangun()
