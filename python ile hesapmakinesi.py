print("""

*******************************
HESAP MAKÝNESÝ
*******************************
1 = TOPLAMA 
2 = ÇIKARMA
3 = ÇARPMA
4 = BÖLME

Örn:Ýþlem yerine 1 ,toplama,Toplama,TOPLAMA yazarsanýz toplama iþlemi uygulanýr.
*******************************

""")

a =int(input("1.Sayý ="))
b =int(input("2.Sayý ="))
islem=(input("islem seç ="))
if islem =="1" or islem == "toplama" or islem =="Toplama" or islem =="TOPLAMA":
    sonuc= a+b
    print("Sonuç =",sonuc)

elif islem =="2" or islem == "çýkarma" or islem =="Çýkarma" or islem =="ÇIKARMA":
    sonuc= a-b
    print("Sonuç =",sonuc)

elif islem =="3" or islem == "çarpma" or islem =="Çarpma" or islem =="ÇARPMA":
    sonuc= a*b
    print("Sonuç =",sonuc)

elif islem =="4" or islem == "bölme" or islem =="Bölme" or islem =="BÖLME":
    sonuc= a/b
    print("Sonuç =",sonuc)
else:
    print("Yanlýþ Ýþlem deðeri girdiniz")