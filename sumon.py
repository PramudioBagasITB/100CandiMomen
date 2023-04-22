jin_db = {}

def summon_jin():
   
    print("Jenis jin yang dapat dipanggil:")
    print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print("(2) Pembangun - Bertugas membangun candi")
    jenis = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
    while jenis not in ["1", "2"]:
        jenis = input("Tidak ada jenis jin bernomor '" + jenis + "'. Masukkan nomor jenis jin yang ingin dipanggil: ")
    if jenis == "1":
        jenis_jin = "Pengumpul"
    elif jenis == "2":
        jenis_jin = "Pembangun"
    
    username = input("Masukkan username jin: ")
    while username in jin_db:
        username = input("Username '" + username + "' sudah diambil. Masukkan username jin: ")
    
    password = input("Masukkan password jin (5-25 karakter): ")
    while len(password) < 5 or len(password) > 25:
        password = input("Password panjangnya harus 5-25 karakter! Masukkan password jin: ")
    
  
    print("Mengumpulkan sesajen...")
    print("Menyerahkan sesajen...")
    print("Membacakan mantra...")
    print("Jin '" + username + "' berhasil dipanggil!")
    
    jin_db[username] = {"jenis": jenis_jin, "password": password}
    

    if len(jin_db) >= 100:
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    

def hilangkan_jin():
    username = input("Masukkan username jin: ")
    if username not in jin_db:
        print("Tidak ada jin dengan username tersebut.")
    else:
        konfirmasi = input("Apakah anda yakin ingin menghapus jin dengan username " + username + " (Y/N)? ")
        if konfirmasi.upper() == "Y":
            del jin_db[username]
            print("Jin telah berhasil dihapus dari alam gaib.")

def ubah_jin():
    username = input("Masukkan username jin : ")
    
    if username not in jin_db:
        print("Tidak ada jin dengan username tersebut.")
        return

    tipe_jin = jin_db[username]["jenis"]
    print("Jin",username, "bertipe", tipe_jin)

    ubah = input('apakah anda ingin merubah tipe jin ini? (y/n)')
    if ubah == 'y' and tipe_jin == 'Pengumpul':
        jin_db[username]["jenis"] = 'Pembangun'
        print('jin', username, 'berhasil diubah dari jin Pengumpul menjadi Pembangun')
    elif ubah == 'y' and tipe_jin == 'Pembangun':
        jin_db[username]["jenis"] = 'Pengumpul'
        print('jin', username, 'berhasil diubah dari jin Pembangun menjadi Pengumpul')

def cek_jin():
    if jin_db == {}:
        print('tidak ada data jin yang disummon')
    else :
        print(jin_db)
