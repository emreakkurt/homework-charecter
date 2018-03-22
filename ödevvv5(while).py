gunluk_uretilen=200
gunluk_defolu_urun=0
toplam_def_urun=0
i=0
while(gunluk_defolu_urun<=gunluk_uretilen*0.20):
    gunluk_defolu_urun=int(input("Günlük defolu ürün miktarı:"))
    toplam_def_urun=toplam_def_urun+gunluk_defolu_urun
    i=i+1
    if(gunluk_defolu_urun>=gunluk_uretilen*0.20):
        print("defolu ürün sayısı günlük limiti aştı")
        break
    print(i,"Günlük","Defolu Ürün sayııs:",toplam_def_urun)
