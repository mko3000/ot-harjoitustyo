import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_kassassa_rahaa_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisia_lounaita_myyty_alussa_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaita_lounaita_myyty_alussa_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateisosto_toimii_edullisesti(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_toimii_maukkaasti(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_ei_toimi_edullisesti(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(239), 239)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_ei_toimi_maukkaasti(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(399), 399)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_toimii_edullisesti(self):
        kortti = Maksukortti(1240)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(str(kortti), 'Kortilla on rahaa 10.00 euroa')

    def test_korttiosto_ei_toimi_edullisesti(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(str(kortti), 'Kortilla on rahaa 1.00 euroa')

    def test_korttiosto_toimii_maukkaasti(self):
        kortti = Maksukortti(1400)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(str(kortti), 'Kortilla on rahaa 10.00 euroa')

    def test_korttiosto_ei_toimi_maukkaasti(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(str(kortti), 'Kortilla on rahaa 1.00 euroa')

    def test_kortille_lataus_toimii(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
        self.assertEqual(str(kortti), 'Kortilla on rahaa 2.00 euroa')

    def test_kortille_negatiivinen_lataus_ei_toimi(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, -1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(kortti), 'Kortilla on rahaa 1.00 euroa')