for i in range(2,100):

    asalmi = True

    for j in range(2,i):
        if i%j==0:
            asalmi= False


    if asalmi==True:
        print ("Asal Sayý:", i)

#YADA
toplam=0
for i in range(2,100):

    asalmi = True

    for j in range(2,i):
        if i%j==0:
            asalmi= False


    if asalmi==True:
        print ("Asal Sayý:", i)
        toplam+=1
print("  ","\t\t+_____\n")
print("toplam =  ",toplam,"tane sayý var")