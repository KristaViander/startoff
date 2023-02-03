import fitness

# Luokkamääritykset (class definitions)
# -------------------------------------

class Kuntoilija:
    """Luokka kuntoilijan tietoja varten"""

    # Olionmuodostin eli  konstruktori
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):

        # Määritellään tulevan olion ominaisuudet (property), luokan kentät (fitness)
        self.nimi = nimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli
        self.bmi = fitness.laske_bmi(self.paino, self.pituus)

    # Metodi rasvaprosentin laskemiseen (aikuinen)
    def rasvaprosentti(self):
        rasvaprosentti = fitness.aikuisen_ravaprosentti(self.bmi, self.ika, self.sukupuoli)
        return self.rasvaprosentti

if __name__ == "__main__":
    
    # Luodaan oli luokasta Kuntoilija
    kuntoilija = Kuntoilija('Kalle Kuntoilija', 171, 65, 40, 1)
    print(kuntoilija.nimi, 'painaa', kuntoilija.paino, 'kg')
    # print('painoindeksi on ', kuntoilija.painoindeksi())
    print('rasvaprosentti on', kuntoilija.rasvaprosentti())
