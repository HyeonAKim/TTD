from django.test import TestCase

# Create your tests here.

# from django.core.urlresolvers import resolve
# 업그레이드 되면서 없어짐

from django.urls import reverse
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = reverse('/')
        self.assertEqual(found.func, home_page)