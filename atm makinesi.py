print("""
************
ATM MAKÝNESÝ

Miktar Sorgulama iþlemi için " 1 " iþlemini seçiniz..
Para Yatýrma iþlemi için " 2 " iþlemini seçiniz..
Para Çekme iþlemi için " 3 " iþlemini seçiniz..

Çýkýþ için "çýkýþ" iþlemini seçiniz...
************
""")
bakiye = 1000
while True: """Bu döngünün çýkýþ yapýlmadan bitmemesini saðlar """

    islem=(input("Ýþlem seçiniz = "))
    if (islem == "1"):
        print ("Hesaptaki bakiye = {}".format(bakiye))

    elif(islem =="2"):
        yatýrýlan =int(input("Yatýrýlacak Miktarý Girin = "))

        bakiye+=yatýrýlan
        print ("hesabýnýza",yatýrýlan,"Tl yatýrýlmýþtýr .")
        print("Toplam Bakiye = ",bakiye)


    elif(islem =="3"):
        cekilen=int(input("Çekmek istediðiniz Miktar = "))
        if (bakiye - cekilen <0):
            print("Bu miktarda para çekemezsiniz! ! ")
            print ("Hesabýnýzdaki Bakiye = ", bakiye,"\n")
            continue
        bakiye-=cekilen

    elif(islem == "çýkýþ"):
        print("Çýkýþ Yapýldý")
        break

    else:
        print("Geçersiz Ýþlem Seçtiniz ")