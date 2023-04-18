import csv
import RNG as rand
bahan = open("bahan_bangunan.csv", 'w', newline=' ')
writer = csv.writer(bahan, delimiter=',')
cols = ['nama', 'deskripsi', 'jumlah']
def kumpul(x) : 
    if x == "indiv" : # jin pengumpul indiv
        pasir = rand()
        batu = rand()
        air = rand()
        print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
        # isi file dalam csv bahan
        #writer.writerow({'nama': '', 'deskripsi': '', 'jumlah' : ''})
        #writer.writerow({'nama': '', 'deskripsi': '', 'jumlah' : ''})
        #writer.writerow({'nama': '', 'deskripsi': '', 'jumlah' : ''})
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
            # isi dalam file csv bahan
            #writer.writerow({'nama': '', 'deskripsi': '', 'jumlah' : ''})
            #writer.writerow({'nama': '', 'deskripsi': '', 'jumlah' : ''})
            #writer.writerow({'nama': '', 'deskripsi': '', 'jumlah' : ''})
        else : # tidak ada jin pengumpul
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")

def bangun() : 
    n = # jumlah jin pembangun
    if n > 0 : # jika ada jin pembangun
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
        # check kesesuaian jumlah material dari csv file 
        if sumpas <= pasir_dari_csv and sumbat <= batu_dari_csv and sumair <= air_dari_csv :
            print(f"Mengerahkan {n} jin untuk membangun candi dengan total bahan {sumpas} pasir, {sumbat} batu, dan {sumair} air")
            print(f"Jin berhasil membangun total {n} candi")
            # kurangi material di csv bahan
            # save candi yang udah dibangun di csv candi
        else : # jumlah material di csv tidak mencukupi
            print("Bangun gagal. Kurang ", end="")
            if sumpas > pasir_dari_csv and sumbat <= batu_dari_csv and sumair <= air_dari_csv : # cuma pasir yang kurang
                print(f"{sumpas-pasir_dari_csv} pasir.")
            elif sumbat > batu_dari_csv and sumpas <= pasir_dari_csv and sumair <= air_dari_csv : # cuma batu yang kurang
                print(f"{sumbat-batu_dari_csv} batu.")
            elif sumair > air_dari_csv and sumpas <= pasir_dari_csv and sumbat <= batu_dari_csv : # cuma air yang kurang
                print(f"{sumair-air_dari_csv} air.")
            elif sumpas > pasir_dari_csv and sumbat > batu_dari_csv and sumair <= air_dari_csv :  # pasir dan batu kurang
                print(f"{sumpas-pasir_dari_csv} pasir, dan {sumbat-batu_dari_csv} batu.")
            elif sumpas > pasir_dari_csv and sumair > air_dari_csv and sumbat <= batu_dari_csv : # pasir dan air kurang
                print(f"{sumpas-pasir_dari_csv} pasir, dan {sumair-air_dari_csv} air.")
            elif sumbat > batu_dari_csv and sumair > air_dari_csv and sumpas <= pasir_dari_csv : # batu dan air kurang
                print(f"{sumbat-batu_dari_csv} batu, dan {sumair-air_dari_csv} air.")
            else : # semua bahan kurang
                print(f"{sumpas-pasir_dari_csv} pasir, {sumbat-batu_dari_csv} batu, dan {sumair-air_dari_csv} air.")
    else : # tidak ada jin pembangun
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
            
