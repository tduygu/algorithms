

def KisiDurumunuVer(toplamTutar, odenenler):
    odenmesiGereken = toplamTutar / len(odenenler)
    print(f"Ödenmesi gereken kişi başı miktar: {odenmesiGereken}")
    for i in range(len(odenenler)):
        n = odenenler[i] - odenmesiGereken
        print(f"{i+1}. kişi {odenenler[i]} TL ödemiş. {abs(n)} TL {'fazla' if n>0 else 'eksik'}")

KisiDurumunuVer(12241,[8941,3300,0])
KisiDurumunuVer(11200, [11200,0])



