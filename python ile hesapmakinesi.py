print("""

*******************************
HESAP MAK�NES�
*******************************
1 = TOPLAMA 
2 = �IKARMA
3 = �ARPMA
4 = B�LME

�rn:��lem yerine 1 ,toplama,Toplama,TOPLAMA yazarsan�z toplama i�lemi uygulan�r.
*******************************

""")

a =int(input("1.Say� ="))
b =int(input("2.Say� ="))
islem=(input("islem se� ="))
if islem =="1" or islem == "toplama" or islem =="Toplama" or islem =="TOPLAMA":
    sonuc= a+b
    print("Sonu� =",sonuc)

elif islem =="2" or islem == "��karma" or islem =="��karma" or islem =="�IKARMA":
    sonuc= a-b
    print("Sonu� =",sonuc)

elif islem =="3" or islem == "�arpma" or islem =="�arpma" or islem =="�ARPMA":
    sonuc= a*b
    print("Sonu� =",sonuc)

elif islem =="4" or islem == "b�lme" or islem =="B�lme" or islem =="B�LME":
    sonuc= a/b
    print("Sonu� =",sonuc)
else:
    print("Yanl�� ��lem de�eri girdiniz")