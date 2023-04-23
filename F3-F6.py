a= input('>>> ')
if a=='summonjin':
        def summonjin():
        print('''Jenis jin yang dapat dipanggil:
        (1) Pengumpul - Bertugas mengumpulkan bahan bangunan
        (2) Pembangun - Bertugas membangun candi''')
        temp=0
        b=int(input('Masukkan nomor jenis jin yang ingin dipanggil : '))
        while b != 1 and b != 2:
            print(f'Tidak ada jenis jin bernomor "{b}"!')
            b=int(input('Masukkan nomor jenis jin yang ingin dipanggil : '))
        else:
            if b==1:
                print('Memilih jin "Pengumpul".')
                e='jin_pengumpul'
            elif b == 2:
                print('Memilih jin "Pembangun"')
                e = 'jin_pembangun'
            c = input('Masukkan username jin : ')
            d = input('Masukkan password jin : ')
            while len(d)<5 or len(d)>15:
                print('Password panjangnya harus 5-25 karakter!')
                d=input('Masukkan password jin : ')
            print(f'''
Mengumpulkan sesajen...
Menyerahkan sesajen...
Membacakan mantra

Jin {c} berhasil dipanggil!''')
            for i in range(2,102):
                if arr_result[0][i][0]==i:
                    arr_result[0][i][0],arr_result[0][i][1],arr_result[0][i][2]=c,d,e
                    break
                else:
                    temp+=1
            if temp>0:
                print('Jumlah jin sudah lebih dari 100!')
        return arr_result
    summonjin()

if a=='hapusjin':
    def hapusjin():
        c = input('Masukkan username jin : ')
        temp=0
        for i in range(2,102):
            if arr_result[0][i][0] == c:
                b = input(f'Apakah anda yakin ingin menghapus jin dengan username {a} (Y/N)? ')
                if b.upper() == 'N':
                    print(f'{c} tidak jadi dihapus')
                    break
                elif b.upper()=='Y':
                    for i in range(102):
                        arr_result[1][i][0], arr_result[1][i][1], arr_result[1][i][2], arr_result[1][i][3], arr_result[1][i][4] = i, '', 0, 0, 0
                    arr_result[0][i][0], arr_result[0][i][1], arr_result[0][i][2] = i, '', ''
                    print('Jin telah dimusnahkan dari alam semesta')
                    break
            else:
                temp += 1
        if temp==100:
            print('Tidak ada jin dengan username tersebut')
        return arr_result
    hapusjin()

if a=='ubahjin':
    def ubahjin():
        c = input('Masukkan username jin : ')
        temp = 0
        for i in range(2,102):
            if arr_result[0][i][0] == c:
                if arr_result[0][i][2]=='jin_pengumpul':
                    pengumpul=input('Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ')
                    if pengumpul.upper()=='N':
                        print('Jin tidak jadi diubah.')
                        break
                    elif pengumpul.upper()=='Y':
                        arr_result[0][i][2]='jin_pembangun'
                        print('Jin telah berhasil diubah.')
                elif arr_result[0][i][2]=='jin_pembangun':
                    pembangun=input('Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ')
                    if pembangun.upper() == 'N':
                        print('Jin tidak jadi diubah.')
                        break
                    elif pembangun.upper() == 'Y':
                        arr_result[0][i][2] = 'jin_pengumpul'
                        print('Jin telah berhasil diubah.')
                break
            else:
                temp+=1
                if temp==100:
                    print('Tidak ada jin dengan username tersebut.')
        return arr_result
    ubahjin()

if a=='bangun':
    def bangun():
        from Fungsi Tambahan import matrix_csv, jml_rows
        matrix = matrix_csv()
        jml_rows=jml_rows()
        temp = 0
        list=[3,4,5] #Contoh List bahan bangunan
        for i in range(1,jml_rows):
            matrix[i][2] = int(matrix[i][2])
            if matrix[i][0] == 'pasir':
                if matrix[i][2]-list[0]<0:
                    temp+=1
                else:
                    matrix[i][2]-=list[0]
            elif matrix[i][0] == 'batu':
                if matrix[i][2]-list[1]<0:
                    temp+=1
                else:
                    matrix[i][2]-=list[1]
            elif matrix[i][0] == 'air':
                if matrix[i][2]-list[2]<0:
                    temp+=1
                else:
                    matrix[i][2]-=list[2]
        if temp!=0:
            print('Bahan bangunan tidak cukup')
            print('Candi tidak berhasil dibangun')
        else:
            print('Candi berhasil dibangun')
    bangun()


