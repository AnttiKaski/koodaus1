# Pythonin kirjastosta hakeminen esimerkki "import time"

from pprint import pformat, pprint
from time import ctime
from time import time


#aikaleima = time.time()

#print (aikaleima)

#aikateksti = time.ctime(aikaleima)

#print(aikateksti)

#aika1=time.time()


#time.sleep(3)

#aika2=time.time()

#print(aika1)
#print(aika2)
#print(aika2-aika1)

aikaleima = time.time()

esimerkki_kuvio={
    "nimi": "Esimerkki",
    "tyyppi": "monikulmio",
    "luotu": ctime(aikaleima),
    "pisteet": [
        {"x": 10, "y": 20, "z": 30},
        {"x": 20, "y": 5, "z": 10},
        {"x": 30, "y": 15. "z": 20}
    ]
}

pprint.pprint(esimerkki_kuvio, sort_dicts=False)

esimerkki_kuvio_muotoiltu_teksti = pformat(esimerkki_kuvio)

#Muutetaan muotoiltu tkesti isoiksi kirjaimiksi ja tulostetaan
# huom:\n = rivivaihto
print("Muotoiltu teksti:\n", esimerkki_kuvio_muotoiltu_teksti.upper())
