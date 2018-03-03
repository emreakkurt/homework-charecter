a=int(input("Planlanmış Üretim Süresini Giriniz:"))
b=int(input("Plansız Duruş süresini Giriniz:"))
c=int(input("Planlanmış Üretim Süresi:"))
d=int(input("Standart Çevrim Zamanını giriniz:"))
e=int(input("Üretim Miktarını Giriniz:"))
g=int(input("Planlanmış Üretim Süresini Giriniz:"))
f=int(input("Plansız Duruş Süresini Giriniz:"))
h=int(input("Sağlam Ürün Miktarını Giriniz:"))
k=int(input("Toplam Üretim Miktarını Giriniz:"))
def kullanılabilirlik():
    kullanılabilirlik=(a-b)/c
    return kullanılabilirlik
def performans():
    performans=(d*e)/(g-f)
    return performans
def kalite():
    kalite=h*k
    return kalite
def oee():
    oee=kullanılabilirlik()*performans()*kalite()
    return oee
    

