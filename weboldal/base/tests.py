from django.contrib.auth.models import User, AnonymousUser
from django.test import TestCase,RequestFactory
from .models import *
from .forms import *


class PostTestCase(TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.factory = None

    def setUp(self):
        self.user1 = User.objects.create_user(username="testuser", password="testuser")
        print("user created", self.user1.username)
        Jegy2.objects.create(nevID="probaJegy", elem="tűz")
        print(Jegy2.objects.all())

    def test_post_is_posted(self):
        """Posts are created"""
        post1 = Jegy2.objects.get(nevID="probaJegy")
        self.assertEqual(post1.elem, "tűz")


class CreateObjects(TestCase):
    def test_haz_koveto(self):
        Haz2.objects.create(nevID="1", leiras="",tipus="követő", mundan_jegye="kos")
        haz_1 = Haz2.objects.get(nevID="1")
        self.assertEqual(haz_1.tipus, 'követő')

    def test_jegy_evszak(self):
        Jegy2.objects.create(nevID="kos", leiras="",elem="tűz",
                             minoseg="kardinális", paritas="pozitív",evszak="tavasz"
                             ,uralkodo_bolygo="mars" )
        kos = Jegy2.objects.get(nevID="kos")
        self.assertEqual(kos.evszak, 'tavasz')

    # def test_jegy_evszak_elirva(self):
    #     # todo meg se lenne szabad engedni hogy a tavaszct meg lehessen adni mint lehetőség
    #     Jegy2.objects.create(nevID="kos", leiras="",elem="tűz",
    #                          minoseg="kardinális", paritas="pozitív",evszak="tavaszc"
    #                          ,uralkodo_bolygo="mars" )
    #
    #     kos = Jegy2.objects.get(nevID="kos")
    #     self.assert(kos.evszak, 'tavasz')

    def test_bolygo_tipus(self):
        Bolygo2.objects.create(nevID="nap", leiras="", tipus="személyjelölő", pontertek="2")
        nap = Bolygo2.objects.get(nevID="nap")
        self.assertEqual(nap.tipus, 'személyjelölő')

    def test_bolygojegyben_kosnap_in_bolygojegyek(self):
        Jegy2.objects.create(nevID="kos", leiras="",elem="tűz",minoseg="kardinális",
                             paritas="pozitív",evszak="tavasz", uralkodo_bolygo="mars" )
        kos = Jegy2.objects.get(nevID="kos")

        Bolygo2.objects.create(nevID="nap", leiras="", tipus="személyjelölő", pontertek="2")
        nap = Bolygo2.objects.get(nevID="nap")

        BolygoJegyben2.objects.create(leiras="", bolygo=nap, jegy=kos)
        bolygojegyek = BolygoJegyben2.objects.all()
        kosnap = BolygoJegyben2.objects.get(bolygo=nap, jegy=kos)
        self.assertIn(kosnap, bolygojegyek)

    def test_quiz_name(self):
        Quiz.objects.create(name= "quiz teszt", desc= "valami leiras", number_of_questions= 3,
                            time= 60, valaszlehetosegek_szama=2 )
        quiz = Quiz.objects.get(id=1)
        self.assertEqual(quiz.name, 'quiz teszt')


class FormTest(TestCase):

    def test_valid(self):
        form_data = {"tulajdonos_neve":"proba1 Név",
                     "idopont": "2001-08-19 16:54",
                     "hely": "Szolnok",
                     "neme": "férfi",
                     "leirasok": "bármi"}
        form = HoroszkopFormGyors(data=form_data)
        self.assertTrue(form.is_valid())

    def test_helytelen_nem(self):
        form_data = {"tulajdonos_neve":"proba1 Név",
                     "idopont": "2001-08-19 16:54",
                     "hely": "Szolnok",
                     "neme": "férfiak",
                     "leirasok": ""}
        form = HoroszkopFormGyors(data=form_data)
        self.assertFalse(form.is_valid())

    def test_helytelen_idoformatum(self):
        form_data = {"tulajdonos_neve":"proba1 Név",
                     "idopont": "2001.08.19. 16:54",  # !!!
                     "hely": "Szolnok",
                     "neme": "férfi",
                     "leirasok": ""}
        form = HoroszkopFormGyors(data=form_data)
        self.assertFalse(form.is_valid())

    def test_helytelen_varos(self):
        """
        Egyenlőre helyes ha rossz még bele kell építeni,
         hogy csak a megadott városokat fogadhassa el
        """
        form_data = {"tulajdonos_neve": "proba1 Név",
                     "idopont": "2001-08-19 16:54",
                     "hely": "otthon",  # !!!
                     "neme": "férfi",
                     "leirasok": ""}
        form = HoroszkopFormGyors(data=form_data)
        self.assertFalse(form.is_valid())

