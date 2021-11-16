import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):

    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(str(self.maksukortti), None)

    def test_saldo_on_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_laataminen(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")

    def test_rahan_ottaminen_kun_rahaa_ei_ole_riittävästi(self):
        self.maksukortti.ota_rahaa(12)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_ottaminen_kun_rahaa_on_riittävästi(self):
        self.maksukortti.ota_rahaa(9)
        self.assertEqual(str(self.maksukortti), "saldo: 0.01")

    def test_rahan_ottaminen_palauttaa_oikean_arvon_kun_rahaa_on_riittävästi(self):
        boolean = self.maksukortti.ota_rahaa(9)
        self.assertEqual(boolean, True)

    def test_rahan_ottaminen_palauttaa_oikean_arvon_kun_rahaa_ei_ole_riittävästi(self):
        boolean = self.maksukortti.ota_rahaa(12)
        self.assertEqual(boolean, False)





