import sqlite3
menu="""-------------------------\nHoşgeldinz,\n1-Veri Ekle\n2-Veri Cek\n3-Programdan cik\n-------------------------"""
connect=sqlite3.connect("database.db")
cursor=connect.cursor()
try:
    run="CREATE TABLE urunler(urunAdi TEXT, urunUcreti TEXT)"
    cursor.execute(run)
    print("Tablo olusturuluyor...")
except:
    print("Tablo mevcut islemlere gecebilirsiniz.")

while True:
    print(menu)
    secim=int(input("Seciminizi Belirtin :==: "))

    if secim == 1:
        urunAdi=input("Eklemek istediginiz urunun adini giriniz :==: ")
        urunFiyati=input("Eklemek istediginiz urunun fiyatini giriniz :==: ")
        run="INSERT INTO urunler (urunAdi, urunUcreti) VALUES ('{}','{}')".format(urunAdi,urunFiyati)
        cursor.execute(run)
        connect.commit()
        print("urun basariyla eklendi.")

    if secim == 2:
        run="SELECT * FROM urunler"
        cursor.execute(run)
        cikti=cursor.fetchall()  
        for i in cikti:
            print("Urun:"+i[0]+" Fiyat:"+i[1]) 

    if secim == 3:
        break    