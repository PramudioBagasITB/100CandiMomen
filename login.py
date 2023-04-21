def read_user():
    global arr_login
    f = open("user.csv", 'r')
    arr_login = [['', '', ''] for x in range(102)]
    f.readline()

    for i in range(102):
        line = f.readline()
        arr_login[i] = line.split(";") #['Bondowoso'; 'cintaroro'; 'bandung_bondowoso']

        if not line:
            break

    f.close()
    return arr_login


username_status = False
password_status = False
login_status = False


def cek_login(arr):
    global username_status, password_status, temp
    for i in range(102):
        temp = arr[i]
        if username == temp[0]:
            username_status = True
            if password == temp[1]:
                password_status = True


def login():
    global username, password, login_status, username_status, password_status
    if not login_status:
        username = input("Username: ")
        password = input("Password: ")
        arr_user = read_user()
        cek_login(arr_user)

        if username_status:
            if password_status:
                login_status = True
                print(f'Selamat datang, {username}!')
                print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
                print('')
            else:
                print("Password salah!")
                username_status = False
                password_status = False
                print('')
        else:
            print("Username tidak terdaftar!")
            username_status = False
            password_status = False
            print('')
    else:
        print('Login gagal!')
        print(f'Anda telah login dengan username {username}, silahkan lakukan “logout” sebelum melakukan login kembali.'
              )
        print('')


def logout():
    global login_status, username_status, password_status
    if login_status:
        username_status = False
        password_status = False
        login_status = False
    else:
        print('Logout gagal!')
        print('Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout')

def ambil_status_login():
    return login_status