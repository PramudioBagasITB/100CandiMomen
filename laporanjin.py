import csv
bahan = open("bahan_bangunan.csv", 'r')
readerB = csv.reader(bahan, delimiter=',')
candi = open("candi.csv", 'r')
readerC = csv.reader(candi, delimiter=',')
user = open("user.csv", 'r')
readerU = csv.reader(user, delimiter=',')

def laporanjin() : 
    # total jin : ...
    totJin = 0 
    rowU = next(readerU)
    while not EOP(rowU) : 
        if rowU[0] != "Bondowoso" or rowU[0] != "Roro":
            totJin += 1
    print("Total Jin: " + str(totJin)) # hitungan total jin

    # total jin pengumpul : ...
    totJinkum = 0
    rowU2 = next(readerU) 
    while not EOP(rowU2) :
        if rowU2[2] == "jin_pengumpul" :
            totJinkum += 1
    print("Total Jin Pengumpul: " + str(totJinkum))
    
    # total jin pembangun : ...
    totJinban = 0 
    rowU3 = next(readerU)
    while not EOP(rowU3) :
        if rowU3[2] == "jin_pembangun" :
            totJinban += 1
    print("Total Jin Pembangun: " + str(totJinban))
    
    # nama jin terajin : ...
    listCan = [["*"] for i in range(totJinban)]
    
    
    # nama jin termalas : ...
# jumlah pasir : ...
# jumlah air : ...
# jumlah batu : ...

# if jin pembangun = 0 then -> jin terajin & jin termalas : -
# 
