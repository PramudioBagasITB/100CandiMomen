from save import save
from load import load

arr_result = load()
users = arr_result[0]
candi = arr_result[1]
bahan_bangunan = arr_result[2]


def exit_func():
    isInputValid = False

    while not isInputValid:
        inp = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

        if (inp.upper() == "Y") or (inp.upper() == "N"):
            isInputValid = True

            if inp.upper() == "Y":
                save(users, candi, bahan_bangunan)
