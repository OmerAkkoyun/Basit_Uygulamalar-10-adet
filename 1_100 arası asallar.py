for i in range(2,100):

    asalmi = True

    for j in range(2,i):
        if i%j==0:
            asalmi= False


    if asalmi==True:
        print ("Asal Say�:", i)

#YADA
toplam=0
for i in range(2,100):

    asalmi = True

    for j in range(2,i):
        if i%j==0:
            asalmi= False


    if asalmi==True:
        print ("Asal Say�:", i)
        toplam+=1
print("  ","\t\t+_____\n")
print("toplam =  ",toplam,"tane say� var")