from flask import Flask, render_template, request, redirect, session
import sqlite3
#yurttan ek alltaki satır
import random

app = Flask(__name__)
app.secret_key = "A13Fe"

@app.route("/")
def hello_world():
    if "ad" in session:
        return render_template('index.html')
    else:
        return render_template('login.html')

@app.route("/yusuf")
def yusufun_sayfasi():
    return render_template('yusuf.html')

@app.route("/cikis")
def cikis():
    session["ad"] = None
    session["sifre"] = None
    return redirect("/login")

@app.route("/kaydol")
def kaydol():
    return render_template('kaydol.html')

@app.route("/kayitbilgileri", methods=["POST"])
def kayit():
    isim = request.form["isim"]
    email = request.form["email"]
    sifre = request.form["sifre"]
    baglanti =sqlite3.connect("veriler.db")
    sorgu =f"SELECT * FROM kullanicilar WHERE ad='{isim}'"
    imlec = baglanti.cursor()
    imlec.execute(sorgu)
    kayitlar = imlec.fetchall()
    if len(kayitlar) ==0:
        sorgu =f"INSERT INTO kullanicilar VALUES('{isim}', '{email}', '{sifre}')"
        imlec.execute(sorgu)
        baglanti.commit()
        return render_template("index.html")
    else:
        return render_template("kaydol.html", hata="Bu kullanıcı zaten kayıtlı")

@app.route("/login") 
def login():
    return render_template('login.html')

@app.route("/loginbilgileri", methods=["POST"])
def login_control():
    isim = request.form["isim"]
    sifre = request.form["sifre"]
    baglanti =sqlite3.connect("veriler.db")
    sorgu =f"SELECT * FROM kullanicilar WHERE ad='{isim}'AND  sifre='{sifre}'"
    imlec = baglanti.cursor()
    imlec.execute(sorgu)
    kayitlar = imlec.fetchall()
    if len(kayitlar) == 0:
        hata="kullanıcı bilgileri hatalı"
        return render_template("login.html",hata="kullanıcı bilgileri hatalı")
    else:
        session["ad"] = isim
        session["sifre"] = sifre
        return redirect("/")

@app.route("/urunler")
def urunler():
    baglanti =sqlite3.connect("veriler.db")
    sorgu ="SELECT * FROM urunler"
    imlec = baglanti.cursor()
    imlec.execute(sorgu)
    kayitlar = imlec.fetchall()
    baglanti.close()
    return render_template("urunler.html", urunler=kayitlar)

@app.route("/urunler/sil/<id>")
def urun_sil(id):
    baglanti =sqlite3.connect("veriler.db")
    sorgu =f"DELETE FROM URUNLER WHERE id={int(id)}"
    imlec = baglanti.cursor()
    imlec.execute(sorgu)
    baglanti.commit()
    baglanti.close()
    return redirect("/urunler")


@app.route("/urunler/guncelle/<id>")
def urun_güncelle(id):
    baglanti =sqlite3.connect("veriler.db")
    sorgu =f"SELECT * FROM urunler WHERE id={int(id)}"
    imlec = baglanti.cursor()
    imlec.execute(sorgu)
    kayit = imlec.fetchone()
    baglanti.close()
    return render_template("urun_guncelle.html", urun=kayit)


@app.route("/urunler/guncelle", methods=["POST"])
def urun_kaydet():
    id=request.form["id"]
    kod=request.form["kod"]
    ad=request.form["ad"]
    fiyat=request.form["fiyat"]

    baglanti =sqlite3.connect("veriler.db")
    sorgu =f"UPDATE urunler SET kod='{kod}', ad='{ad}', fiyat={float(fiyat)} WHERE id={int(id)}"
    imlec = baglanti.cursor()
    imlec.execute(sorgu)
    kayit = imlec.fetchone()
    baglanti.commit()
    baglanti.close()
    return redirect("/urunler")
#burdan sonrası yurttan ek  bir sonraki yorum satırına kadar

@app.route("/ekle")
def ekle_sayfasi():
    if "ad" in session:
        return render_template('urun_ekle.html')
    else:
        return render_template('login.html')

@app.route("/urun_ekle", methods=["POST"])
def urun_ekle():
    if "ad" in session:
        kod = request.form["kod"]
        ad = request.form["ad"]
        fiyat = request.form["fiyat"]

        baglanti = sqlite3.connect("veriler.db")
        sorgu = f"INSERT INTO urunler (kod, ad, fiyat) VALUES ('{kod}', '{ad}', {float(fiyat)})"
        
        imlec = baglanti.cursor()
        imlec.execute(sorgu)
        baglanti.commit()
        baglanti.close()

        return redirect("/urunler")
    else:
        return render_template('login.html')

    
#yurttan ek son
app.run(debug=True)