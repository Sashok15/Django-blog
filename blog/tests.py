from django.test import TestCase
from django.urls import reverse
# Create your tests here.


class URLTests(TestCase):
    
    def test_index_page_anonymous(self):
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)

    def test_article_detail_page_anonymous(self):
        url = reverse('detail', args=[52])
        # url = 'article-detail/52/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_anonymous(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        login_pass = self.client.post(
            '/login/', {'username': 'john', 'password': 'smith'})
        self.assertEqual(login_pass.status_code, 200)
