from login import login, logout
from Help import list_help
from save import save
from exit import exit_func
from load import load

arr_result = load()
users = arr_result[0]
candi = arr_result[1]
bahan_bangunan = arr_result[2]


def instruction():
    ins = input("Instruksinya apa a?? : ")
    if ins == "login":
        login()
        instruction()
    elif ins == "logout":
        logout()
        instruction()
    elif ins == "terminate":
        quit()
    elif ins == "help":
        list_help()
        instruction()
    elif ins == "save":
        save(users, candi, bahan_bangunan)
        instruction()
    elif ins == "exit":
        exit_func()
        quit()
