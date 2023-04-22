import os
import time
from write_file import write_user
from write_file import write_bahan
from write_file import write_candi


def save(arr_user, arr_candi, arr_bahan):
    nama_folder = input("Masukkan nama folder: ")
    path = './save/' + nama_folder
    isExist = os.path.isdir(path)

    print("Saving...")
    time.sleep(2)

    if not isExist:
        print(f"Membuat folder save/{nama_folder}...")
        os.mkdir(path)
        time.sleep(2)

    path_user = f'{path}/user.csv'
    path_candi = f'{path}/candi.csv'
    path_bahan = f'{path}/bahan_bangunan.csv'

    print(arr_user)
    print(arr_candi)
    print(arr_bahan)

    write_user(path_user, arr_user)
    write_candi(path_candi, arr_candi)
    write_bahan(path_bahan, arr_bahan)

    print(f"Berhasil menyimpan data di folder save/{nama_folder}!")
