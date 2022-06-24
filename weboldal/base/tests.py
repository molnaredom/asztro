from django.contrib.auth.models import User, AnonymousUser
from django.test import TestCase,RequestFactory
from .models import Jegy2, Bolygo2, Haz2, BolygoJegyben2


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
    def test_haz(self):
        Haz2.objects.create(nevID="1", leiras="",tipus="követő", mundan_jegye="kos")
        haz_1 = Haz2.objects.get(nevID="1")
        self.assertEqual(haz_1.tipus, 'követő')

    def test_jegy(self):
        Jegy2.objects.create(nevID="kos", leiras="",elem="tűz",
                             minoseg="kardinális", paritas="pozitív",evszak="tavasz"
                             ,uralkodo_bolygo="mars" )
        kos = Jegy2.objects.get(nevID="kos")
        self.assertEqual(kos.evszak, 'tavasz')

    def test_jegy_rossz(self):
        # todo meg se lenne szabad engedni hogy a tavaszct meg lehessen adni mint lehetőség
        Jegy2.objects.create(nevID="kos", leiras="",elem="tűz",
                             minoseg="kardinális", paritas="pozitív",evszak="tavaszc"
                             ,uralkodo_bolygo="mars" )

        kos = Jegy2.objects.get(nevID="kos")
        self.assertNotEqual(kos.evszak, 'tavasz')

    def test_bolygo(self):
        Bolygo2.objects.create(nevID="nap", leiras="", tipus="személyjelölő", pontertek="2")
        nap = Bolygo2.objects.get(nevID="nap")
        self.assertEqual(nap.tipus, 'személyjelölő')

    def test_bolygojegyben(self):
        Jegy2.objects.create(nevID="kos", leiras="",elem="tűz",minoseg="kardinális",
                             paritas="pozitív",evszak="tavasz", uralkodo_bolygo="mars" )
        kos = Jegy2.objects.get(nevID="kos")

        Bolygo2.objects.create(nevID="nap", leiras="", tipus="személyjelölő", pontertek="2")
        nap = Bolygo2.objects.get(nevID="nap")

        BolygoJegyben2.objects.create(leiras="", bolygo=nap, jegy=kos)
        bolygojegyek = BolygoJegyben2.objects.all()
        kosnap = BolygoJegyben2.objects.get(bolygo=nap, jegy=kos)
        self.assertIn(kosnap, bolygojegyek)

    # def test_bolygohazban(self):
    #     Jegy2.objects.create(nevID="kos", leiras="",elem="tűz",
    #                          minoseg="kardinális", paritas="pozitív",evszak="tavasz"
    #                          ,uralkodo_bolygo="mars" )
    #     kos = Jegy2.objects.get(nevID="kos")
    #     self.assertEqual(kos.evszak, 'tavasz')


import datetime

from django.test import TestCase
from django.utils import timezone

from .forms import HoroszkopFormGyors

class FormTest(TestCase):
    def test_renew_form_date_field_label(self):
        form = HoroszkopFormGyors()
        print(form)
        self.assertTrue(form.fields['hely'].label == "")

    def test_renew_form_date_field_help_text(self):
        form = HoroszkopFormGyors()
        self.assertEqual(form.fields['tulajdonos_neve'].help_text, '')

    # def test_renew_form_date_in_past(self):
    #     date = datetime.date.today() - datetime.timedelta(days=1)
    #     form = RenewBookForm(data={'renewal_date': date})
    #     self.assertFalse(form.is_valid())
    #
    # def test_renew_form_date_too_far_in_future(self):
    #     date = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
    #     form = RenewBookForm(data={'renewal_date': date})
    #     self.assertFalse(form.is_valid())
    #
    # def test_renew_form_date_today(self):
    #     date = datetime.date.today()
    #     form = RenewBookForm(data={'renewal_date': date})
    #     self.assertTrue(form.is_valid())
    #
    # def test_renew_form_date_max(self):
    #     date = timezone.localtime() + datetime.timedelta(weeks=4)
    #     form = RenewBookForm(data={'renewal_date': date})
    #     self.assertTrue(form.is_valid())
