    # Tee koodi, joka kysyy viisi nimeä ja laittaa ne listaan "nimet"

nimet = []

# Ctrl+Shift+P -> VSCoden komentopaletti


# Ctrl + ' rivienkommentointi

# for i in range(1.6):
#   nimi = input("Anna nimi " + str(i)+ ": ")
#   nimi.append(nimi)


#           Vaihtoehto 1
while True:
    nimi = input("Anna nimi: ")
    nimet.append(nimi)
if len(nimet) >= 5:
    break

#           Vaihtoehto 2

while len(nimet) < 5:
    nimi = input("Anna nimi: ")
    nimet.append(nimi)
 if len(nimet)

