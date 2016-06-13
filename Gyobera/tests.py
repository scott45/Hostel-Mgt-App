from django.test import TestCase
from django.test import LiveServerTestCase
from django.core.urlresolvers import reverse
from .models import Classification, List, Student, Booking, Room


class IndexViewTests(TestCase):
    def test_index_view_with_no_classifications(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no classifications present.")
        self.assertQuerysetEqual(response.context['classifications'], [])


class HomeViewTests(TestCase):
    def test_home_view(self):
        two = self.client.get(reverse('home'))
        self.assertEqual(two.status_code, 200)
        self.assertContains(two, 'Register Here')


class ClassificationMethodTests(TestCase):
    def test_ensure_views_are_positive(self):
        cat = Classification(name='test', views=1, likes=0)
        cat.save()
        self.assertEqual((cat.views >= 0), True)
