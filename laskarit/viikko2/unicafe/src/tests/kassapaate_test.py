import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(str(self.kassapaate), None)

    def test_kassassa_rahaa_alustettu_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_alustettu_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_alustettu_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # testit syö edullisesti käteisellä

    def test_syö_edullisesti_käteisellä_oikein_kassassa(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_syö_edullisesti_käteisellä_oikeat_määrät(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syö_edullisesti_käteisellä_vaihtoraha_tasan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)

    def test_syö_edullisesti_käteisellä_vaihtoraha_ei_tasan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)

    def test_syö_edullisesti_käteisellä_vaihtoraha_alle(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230), 230)

    # testit syö maukkaasti käteisellä

    def test_syö_maukkaasti_käteisellä_oikein_kassassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_syö_maukkaasti_käteisellä_oikeat_määrät(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syö_maukkaasti_käteisellä_vaihtoraha_tasan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)

    def test_syö_maukkaasti_käteisellä_vaihtoraha_ei_tasan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(450), 50)

    def test_syö_edullisesti_käteisellä_vaihtoraha_alle(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(230), 230)

    # Testit syö edullisesti kortilla

    def test_syö_edullisesti_kortilla_kun_rahaa_on_riittävästi(self):
        maksukortti = Maksukortti(1000)
        boolean = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(boolean, True)

    def test_syö_edullisesti_kortilla_kun_rahaa_ei_ole_riittävästi(self):
        maksukortti = Maksukortti(200)
        boolean = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(boolean, False)

    # Testit syö maukkaasti kortilla

    def test_syö_maukkaasti_kortilla_kun_rahaa_on_riittävästi(self):
        maksukortti = Maksukortti(450)
        boolean = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(boolean, True)

    def test_syö_maukkaasti_kortilla_kun_rahaa_ei_ole_riittävästi(self):
        maksukortti = Maksukortti(200)
        boolean = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(boolean, False)

    # testaa määrien toiminta kortilla

    def test_syö_maukkaasti_kortilla_määrä_on_oikein_kun_ei_ole_riittävästi(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syö_edullisesti_kortilla_määrä_on_oikein_kun_rahaa_riittävästi(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syö_maukkaasti_kortilla_määrä_on_oikein_kun_ei_ole_riittävästi(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syö_maukkaasti_kortilla_määrä_on_oikein_kun_rahaa_riittävästi(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    # kortilla oikeat arvot

    def test_syö_maukkaasti_kortilla_oikein_kun_rahaa_riittävästi(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 600)

    def test_syö_maukkaasti_kortilla_oikein_kun_ei_ole_riittävästi(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 200)

    def test_syö_maukkaasti_kortilla_oikein_kun_rahaa_riittävästi(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 760)

    def test_syö_maukkaasti_kortilla_oikein_kun_ei_ole_riittävästi(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 200)

    # testaa rahan lataamista kortille

    def test_lataa_rahaa_oikein_kassassa(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 250)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100250)

    def test_lataa_rahaa_palauttaa_oikein_kun_summa_on_negatiivinen(self):
        maksukortti = Maksukortti(1000)
        boolean = self.kassapaate.lataa_rahaa_kortille(maksukortti, -250)
        self.assertEqual(boolean, None)

    def test_lataa_rahaa_oikein_kassassa_kun_summa_on_negatiivinen(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -250)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_rahaa_oikein_kortille(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 250)
        self.assertEqual(maksukortti.saldo, 1250)
