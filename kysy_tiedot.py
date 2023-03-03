# Ohjelma, joka kyssy bmi-tietoja useasta kuntoilijasta
# =====================================================



import fitness


# Kysytään tiedot ja tulostetaan paiindeksi kunnes halutaan lopettaa
bmi_lista = []
nimilista = []
while True: # Ikuinen silmukka, jossa ollaan kunnes annetaan tyhjä nimi

    nimi = input('Nimi, tyhjä lopettaa: ')

    if nimi == '':
        break

    nimilista.append(nimi)
    pituus_teksti = input('Pituus (cm) ')
    paino_teksti = input('Paino (kg): ')

    # Yritwtään muuttaa syötetyt tekstit luvuiksi ja laskea BMI
    try:
        pituus = float(pituus_teksti)
        paino = float(paino_teksti)

        #Lasketaan painoindeksi fitness-moduulin laske_bmi-funktiolla
        bmi = fitness.laske_bmi(paino. pituus)

        # 
        monikko = (nimi, bmi)

        # Lisätään monikko listaan
        

        # Näytetään tulokset ruudulla
