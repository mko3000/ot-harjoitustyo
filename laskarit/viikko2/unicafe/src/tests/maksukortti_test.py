import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), 'Kortilla on rahaa 10.00 euroa' )
    
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), 'Kortilla on rahaa 11.00 euroa' )

    def test_saldo_ei_muutu_jos_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(1001)
        self.assertEqual(str(self.maksukortti), 'Kortilla on rahaa 10.00 euroa' )

    def test_metodi_palauttaa_true_jos_raha_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100), True)

    def test_metodi_palauttaa_false_jos_raha_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1001), False)

    
