print("""
************************
Kullanýcý Giriþi Sistemi
************************

""")
sys_kullanici_adi="omer"
sys_sifre="12345"
deneme_hakki = 3

while True:
    kullanici_adi=input("kullanýcý adý= ")
    sifre=input("þifre =")

    if(kullanici_adi != sys_kullanici_adi and sifre ==sys_sifre):
        print("Kullanýcý adý Hatalý")
        deneme_hakki-= 1

    elif (kullanici_adi == sys_kullanici_adi and sifre !=sys_sifre):
        print("Yanlýþ Þifre")
        deneme_hakki-= 1

    elif (kullanici_adi != sys_kullanici_adi and sifre != sys_sifre):
        print("Yanlýþ Þifre ve Yanlýþ kullanýcý adý")
        deneme_hakki-= 1
    else:
        print("Giriþ Baþarýlý")
        break

    if deneme_hakki == 0:
        print("3 yanlýþ giriþ...Giriþ Denemesi Baþarýsýz!")
        break