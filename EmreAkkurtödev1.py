finansmanGeliri=int(input("Finansman Gelirini giriniz:"))
pazarGeliri=int(input("Pazar Gelirini giriniz:"))
kiraGeliri=int(input("Kira Giderini giriniz:"))
ucret=int(input("Ücret giriniz"))
finansmanGideri=int(input("Finansman Giderini giriniz"))
pazarGideri=int(input("Pazar giderini giriniz"))
kiraGideri=int(input("Kira Giderini giriniz"))
muhasebeGideri=int(input("Muhasebe giderini giriniz"))
gelir=finansmanGeliri+pazarGeliri+kiraGeliri
gider=ucret+finansmanGideri+pazarGideri+kiraGideri+muhasebeGideri
if gelir>1000:
    print("İşletme Kâr etmiştir")
else :
    print("İşletme Zarara uğraşmıştır")
    
