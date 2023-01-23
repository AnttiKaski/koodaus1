import Harjoitus2 as H2
from Harjoitus2 import kysy_nimet

if __name__== "__main__":
    joku_juttu = 1

    print("Kysytään 2 nimeä:")
    nimet = H2.kysy_nimet(2)
    joku_juttu = 2
    nimet.append("Ekstra nimi")
    joku_juttu = 3
    print ("Nimet ovat", nimet)
