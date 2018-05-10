from django.test import TestCase
from django.urls import reverse, resolve
from .views import home, board_topics
from .models import Board



# Create your tests here.

class HomeTests(TestCase):

    def setUp(self):
        self.board = Board.objects.create(name='Django', description='djnag xx')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_status(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_view_contains_link(self):
        topic_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(topic_url))


class TopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name="Django", description="d board")

    def test_board_topics_view_success(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200);

    def test_board_topics_url_resolve_views(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)

    def test_board_topics_view_contains_back_to_homepage(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        homepage_url = reverse('home')
        self.assertEquals(response, 'href="{0}"'.format(homepage_url) )
