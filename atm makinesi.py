print("""
************
ATM MAK�NES�

Miktar Sorgulama i�lemi i�in " 1 " i�lemini se�iniz..
Para Yat�rma i�lemi i�in " 2 " i�lemini se�iniz..
Para �ekme i�lemi i�in " 3 " i�lemini se�iniz..

��k�� i�in "��k��" i�lemini se�iniz...
************
""")
bakiye = 1000
while True: """Bu d�ng�n�n ��k�� yap�lmadan bitmemesini sa�lar """

    islem=(input("��lem se�iniz = "))
    if (islem == "1"):
        print ("Hesaptaki bakiye = {}".format(bakiye))

    elif(islem =="2"):
        yat�r�lan =int(input("Yat�r�lacak Miktar� Girin = "))

        bakiye+=yat�r�lan
        print ("hesab�n�za",yat�r�lan,"Tl yat�r�lm��t�r .")
        print("Toplam Bakiye = ",bakiye)


    elif(islem =="3"):
        cekilen=int(input("�ekmek istedi�iniz Miktar = "))
        if (bakiye - cekilen <0):
            print("Bu miktarda para �ekemezsiniz! ! ")
            print ("Hesab�n�zdaki Bakiye = ", bakiye,"\n")
            continue
        bakiye-=cekilen

    elif(islem == "��k��"):
        print("��k�� Yap�ld�")
        break

    else:
        print("Ge�ersiz ��lem Se�tiniz ")