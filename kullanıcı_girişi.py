print("""
************************
Kullan�c� Giri�i Sistemi
************************

""")
sys_kullanici_adi="omer"
sys_sifre="12345"
deneme_hakki = 3

while True:
    kullanici_adi=input("kullan�c� ad�= ")
    sifre=input("�ifre =")

    if(kullanici_adi != sys_kullanici_adi and sifre ==sys_sifre):
        print("Kullan�c� ad� Hatal�")
        deneme_hakki-= 1

    elif (kullanici_adi == sys_kullanici_adi and sifre !=sys_sifre):
        print("Yanl�� �ifre")
        deneme_hakki-= 1

    elif (kullanici_adi != sys_kullanici_adi and sifre != sys_sifre):
        print("Yanl�� �ifre ve Yanl�� kullan�c� ad�")
        deneme_hakki-= 1
    else:
        print("Giri� Ba�ar�l�")
        break

    if deneme_hakki == 0:
        print("3 yanl�� giri�...Giri� Denemesi Ba�ar�s�z!")
        break