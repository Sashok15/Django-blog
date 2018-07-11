from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Article
from .forms import ArticleForm, CommentForm
# Create your tests here.


class URLTests(TestCase):

    def setUp(self):
        # Создание двух пользователей
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_article = Article.objects.create(author=test_user1 ,title='hey', text='text500')

    # @classmethod
    # def setUpTestData(cls):
        # Create 13 authors for pagination tests
        # number_of_authors = 13
        # for author_num in range(number_of_authors):
            # Author.objects.create(first_name='Christian %s' % author_num, last_name = 'Surname %s' % author_num,)
        # Article.objects.create(author=se.client, title='hey', text='text500')

    
    def test_index_page_anonymous(self):
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)

    def test_article_detail_page_anonymous(self):
        url = reverse('detail', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_anonymous(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        login_pass = self.client.post(
            '/login/', {'username': 'john', 'password': 'smith'})
        self.assertEqual(login_pass.status_code, 200)

# class RenewBookFormTest(TestCase):
#     def test_renew_form_date_field_label(self):
#         form = ArticleForm()        
#         self.assertTrue(form.fields['text'].label == None or form.fields['text'].label == 'text')

# class ArticleModelTests(TestCase):
#     pass
