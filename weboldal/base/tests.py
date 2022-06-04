from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from .models import Jegy2
# from .forms import PostForm

class PostTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="testuser")
        print("user created")
        Jegy2.objects.create(nevID="probaJegy", elem="tűz")
        print(Jegy2.objects.all())

    def test_post_is_posted(self):
        """Posts are created"""
        post1 = Jegy2.objects.get(nevID="probaJegy")
        self.assertEqual(post1.elem, "tűz")

        # self.assertEqual(post1.text, "Jegy meglétének tesztelése")

    # def test_valid_form_data(self):
    #     form = PostForm({
    #         'title': "Just testing",
    #         'text': "Repeated tests make the app foul-proof",
    #     })
    #     self.assertTrue(form.is_valid())
    #     post1 = form.save(commit=False)
    #     post1.author = self.user1
    #     post1.save()
    #     self.assertEqual(post1.title, "Just testing")
    #     self.assertEqual(post1.text, "Repeated tests make the app foul-proof")
    #
    # def test_blank_form_data(self):
    #     form = PostForm({})
    #     self.assertFalse(form.is_valid())
    #     self.assertEqual(form.errors, {
    #         'title': ['This field is required.'],
    #         'text': ['This field is required.'],
    #     })
