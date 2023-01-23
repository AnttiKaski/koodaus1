# Tähän mennessä käytettyjä funktioita
# print(X) # Tulostetaan X
# X = input() # Luetaan merkkijono muuttujaan X
# str(X) # muutetaan X merkkijonoksi

# L.append(X) # lisätään listan L loppuun X



def kysy_nimi():
    nimi = input("Anna nimi: ")
    return nimi


def kysy_nimet(lkm):
    nimet = []
    while len(nimet) < lkm:
        nimi = kysy_nimi()
        nimet.append(nimi)
    return nimet


def kysy_nimet_rekursiolla(jäljellä, nimet=None):
    if jäljellä == 0:
        return nimet
    if nimet is None:
        nimet = []
    nimi = kysy_nimi()
    return kysy_nimet_rekursiolla(jäljellä - 1, nimet + (nimi))


nimilista = kysy_nimet(3)
print(nimilista)
