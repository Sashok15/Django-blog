from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase
from django.urls import reverse

from .forms import ArticleForm, CommentForm
from .models import Article, Comment
from selenium.webdriver.firefox.webdriver import WebDriver
# Create your tests here.


class URLTests(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(
            username='testuser1',
            password='12345'
        )
        test_article = Article.objects.create(
            author=test_user, 
            title='hey', 
            text='text500'
            )
        comment = Comment.objects.create(
            author=test_user,
            text='comment',
            article=test_article
        )
        # for i in range(10):
        # test_user1 = User.objects.create_user(username=f'testuser{i}', password='12345')
        # test_article = Article.objects.create(author=test_user1 ,title=f'hey{i}', text='text500')

    def test_index_page_anonymous(self):
        resp = self.client.get('/index/')
        self.assertTemplateUsed(resp, 'blog/index.html')
        self.assertEqual(resp.status_code, 200)
        self.assertNotEqual(resp.status_code, 404)
        self.assertNotContains(resp, ' <a href="/create-article/">CreateArticle</a>')
        self.assertTrue('articles' in resp.context)

    def test_article_detail_page_anonymous(self):
        url = reverse('detail', args=[1])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('article' in resp.context)
        self.assertTrue('comments' in resp.context)

    def test_slash_page_anonymous(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertNotEqual(resp.status_code, 404)
        self.assertTrue('articles' in resp.context)

    def test_login_page(self):
        resp = self.client.post(
            '/login/', {'username': 'testuser1', 'password': '12345'})
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(response=resp, expected_url='/')

    def test_create_article_anonymous(self):
        resp = self.client.post(
            '/create-article/', {'title': 'test_hello', 'text': 'test_text'})
        # print(resp.url)
        self.assertTrue(resp.url.startswith('/login/'))
        # user = self.client.get('/create-article/')
        self.assertEqual(resp.status_code, 302)

    def test_create_article_as_user(self):
        resp = self.client.login(username='testuser1', password='12345')
        res_post = self.client.post(
            '/create-article/', {'title': 'test_hello', 'text': 'test_text'})
        # print(res_post)
        self.assertTrue(resp)
        self.assertTrue(res_post.url.startswith('/'))
        self.assertEqual(res_post.status_code, 302)


class ArticleFormTest(TestCase):

    # def test_form_date_field_label(self):
    #     form = ArticleForm()
    #     self.assertTrue(form.fields['text'] == None or form.fields['text'] == 'text')

    def test_text_form(self):
        test_title, test_data = 'title', 'text'
        form_data = {'title': test_title, 'text': test_data, }
        form = ArticleForm(data=form_data)
        self.assertTrue(form.is_valid())


class CommentFormTest(TestCase):
    def test_text_form(self):
        text = 'test_text'
        form_data = {'text': text}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())


class CommentModelTest(TestCase):

    def test_string_representation(self):
        comment = Comment(text="My comment body")
        self.assertEqual(str(comment), "My comment body")
# class MySeleniumTests(StaticLiveServerTestCase):
#     @classmethod
#     def setUpClass(cls):
#         super(MySeleniumTests, cls).setUpClass()
#         cls.selenium = WebDriver()


#     @classmethod
#     def tearDownClass(cls):
#         cls.selenium.quit()
#         super(MySeleniumTests, cls).tearDownClass()


#     def test_login(self):
#         self.selenium.get('% s % s' % (self.live_server_url, '/login/'))
#         username_input = self.selenium.find_element_by_name('username')
#         username_input.send_keys('myuser')
#         password_input = self.selenium.find_element_by_name('password')
#         password_input.send_keys('secret')
#         self.selenium.find_element_by_xpath('//input[@value=”Log in”]').click()
