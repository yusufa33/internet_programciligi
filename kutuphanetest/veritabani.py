import sqlite3

# veriler.db isimli bir veritabanı yarat
baglanti = sqlite3.connect("veriler.db")

#tablo yaratma, silme ve diğer işlemler için cursor nesnesi yarat
# imlec = baglanti.cursor()
# sorgu = "CREATE TABLE IF NOT EXISTS kullanicilar (ad TEXT, email TEXT, sifre TEXT)"
# #sql sorgusunu çalıştır
# imlec.execute(sorgu)
# #tüm veritabanı işlemlerini uygula, kaydet
# baglanti.commit()


# #tabloya veri kaydet
# sorgu = "INSERT INTO kullanicilar VALUES('dogukan','d@gmail.com','1234')"
# imlec.execute(sorgu)
# baglanti.commit()



sorgu = """CREATE TABLE IF NOT EXISTS     urunler  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                  kod TEXT,
                                                  ad TEXT,
                                                  fiyat REAL)"""
#sql sorgusunu çalıştır
imlec.execute(sorgu)
#tüm veritabanı işlemlerini uygula, kaydet
baglanti.commit()


#tabloya veri kaydet
import random
semboller= "0123456789qwertyuıopğüasdfghjklşizxcvbnmöçQWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ"
urun_kodu = "".join(random.choices(semboller, k=5))

sorgu = f"INSERT INTO urunler (kod, ad, fiyat) VALUES ('{urun_kodu}', 'kahve',10.5)"
imlec.execute(sorgu)
#tüm veritabanı işlemlerini uygula, kaydet
baglanti.commit()