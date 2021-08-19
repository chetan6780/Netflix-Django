from django.test import TestCase

from .models import Video


class VideoModelTestCase(TestCase):
    def setUp(self):
        Video.objects.create(title='Test Title')

    def test_valid_title(self):
        title = 'Test Title'
        qs = Video.objects.filter(title=title)
        self.assertTrue(qs.exists())

    def test_created_count(self):
        qs = Video.objects.all()  # query_set
        self.assertEqual(qs.count(), 1)