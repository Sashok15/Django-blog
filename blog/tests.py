from django.test import TestCase

# Create your tests here.


class URLTests(TestCase):
    
    def test_index_page_anonymous(self):
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)


    def test_article_detail_page_anonymous(self):
        response = self.client.get('/article_detail/55/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_anonymous(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        login_pass = self.client.post(
            '/login/', {'username': 'john', 'password': 'smith'})
        self.assertEqual(login_pass.status_code, 200)

    def funcname(self, parameter_list):
        pass
