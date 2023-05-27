import sqlite3
menu="""-------------------------\nHoşgeldinz,\n1-Veri Ekle\n2-Veri Cek\n3-En pahali Ve En Ucuz Urunleri Getir\n4-Programdan cik\n-------------------------"""
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
        toplam=0
        list=[]
        for i in cikti:
            toplam+=int(i[1])
            print("Urun:"+i[0]+" Fiyat:"+i[1])
            list.append(int(i[1]))
        print("Toplam fiyat :==: ",int(toplam))

    if secim == 3:
        run="SELECT * FROM urunler"
        cursor.execute(run)
        cikti=cursor.fetchall()
        toplam=0
        list=[]
        for i in cikti:
            toplam+=int(i[1])
            list.append(int(i[1]))

        print("kucuk:", min(list))
        print("buyuk:",max(list))

    if secim == 4:
        break