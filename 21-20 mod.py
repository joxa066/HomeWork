# 1 homework

def musbat_sonlarni_tanlash(sonlar):
    musbat_sonlar = []
    for son in sonlar:
        if son > 0:
            musbat_sonlar.append(son)
    return musbat_sonlar


raqamlar = [-2, -6, 0, 3, 8, -5, 10]
musbat_sonlar = musbat_sonlarni_tanlash(raqamlar)
print(musbat_sonlar)