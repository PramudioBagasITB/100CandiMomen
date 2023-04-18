import csv
import RNG as rand
bahan = open("bahan_bangunan.csv", 'w', newline=' ')
writer = csv.writer(bahan, delimiter=',')
cols = ['nama', 'deskripsi', 'jumlah']
def kumpul(x) : 
    if x == 1 : # jin pengumpul indiv
        pasir = rand()
        batu = rand()
        air = rand()
        print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
        # isi dalam file csv bahan
    else : # batch kumpul
        n =  # jumlah jin pengumpul
        if n > 0 : # ada jin pengumpul
            pasir = [0 for i in range(n)]
            batu = [0 for i in range(n)]
            air = [0 for i in range(n)]
            mat = [pasir,batu,air]
            for i in range(3) : 
                for j in range(n) :
                    mat[i][j] = rand()
            sumpas = 0
            sumbat = 0 
            sumair = 0
            for i in range(n) :
                sumpas += mat[0][j]
                sumbat += mat[1][j]
                sumair += mat[2][j]
            print(f"Mengerahkan {n} jin untuk mengumpulkan bahan.")
            print(f"Jin menemukan total {sumpas} pasir, {sumbat} batu, dan {sumair} air.")
        else : # tidak ada jin pengumpul
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")

def bangun(x) : 
    if x == 1 : # jin pembangun indiv
        #
    else : # batch bangun
        #
