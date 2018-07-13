from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase
from django.urls import reverse

from ..forms import ArticleForm, CommentForm
from ..models import Article, Comment
from ..serializers import ArticleSerializer
# Create your tests here.


class URLTests(TestCase):

    def setUp(self):
        self.register_user = {'username': 'testuser1', 'password': '12345'}
        self.user = User.objects.create_user(**self.register_user)
        self.article = Article.objects.create(
            author=self.user,
            title='hey',
            text='text500'
        )
        self.comment = Comment.objects.create(
            author=self.user,
            text='comment',
            article=self.article
        )

    def test_index_page_anonymous(self):
        resp = self.client.get('/index/')
        # print(self.article.id)
        self.assertTemplateUsed(resp, 'blog/index.html')
        self.assertEqual(resp.status_code, 200)
        self.assertNotEqual(resp.status_code, 404)
        self.assertNotContains(
            resp, ' <a href="/create-article/">CreateArticle</a>'
        )
        self.assertTrue('articles' in resp.context)

    def test_slash_page_anonymous(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertNotEqual(resp.status_code, 404)
        self.assertTrue('articles' in resp.context)

    def test_article_detail_page_anonymous(self):
        url = reverse('detail', args=[self.article.id])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('article' in resp.context)
        self.assertTrue('comments' in resp.context)

    def test_article_delete_page_anonymous(self):
        url = reverse('delete_article', args=[self.article.id])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)

    def test_article_delete_page_user(self):
        url = reverse('delete_article', args=[self.article.id])
        is_login = self.client.login(username='testuser1', password='12345')
        resp = self.client.post(
            '/create-article/', {'title': 'test_hello', 'text': 'test_text'})
        # print(resp.url)
        self.assertTrue(is_login)
        self.assertTrue(resp.url.startswith('/index/'))
        self.assertEqual(resp.status_code, 302)

    def test_login_page(self):
        resp = self.client.post(
            '/login/', {'username': 'testuser1', 'password': '12345'}
        )
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(response=resp, expected_url='/')

    def test_create_article_anonymous(self):
        resp = self.client.post(
            '/create-article/', {'title': 'test_hello', 'text': 'test_text'}
        )
        self.assertTrue(resp.url.startswith('/login/'))
        self.assertEqual(resp.status_code, 302)

    def test_create_article_as_user(self):
        url = reverse('create_article')
        is_login = self.client.login(username='testuser1', password='12345')
        resp_get = self.client.get(url)
        self.assertEqual(resp_get.status_code, 200)
        resp = self.client.post(
            url, {'title': 'test_hello', 'text': 'test_text'}
        )
        # print(resp.url)
        self.assertTrue(is_login)
        self.assertTrue(resp.url.startswith('/index/'))
        self.assertEqual(resp.status_code, 302)


class ArticleFormTest(TestCase):

    def setUp(self):
        self.register_user = {'username': 'testuser1', 'password': '12345'}
        self.user = User.objects.create_user(**self.register_user)
        self.article = Article.objects.create(author=self.user, title="My entry title")
        self.form_data = {'title': 'title12', 'text': 'text12', 'author':self.user}


    def test_text_form(self):
        form = ArticleForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    # def test_valid_data(self):
    #     form = ArticleForm(data = self.form_data)
    #     self.assertTrue(form.is_valid())
    #     article = form.save()
    #     self.assertEqual(article.name, "title")
    #     self.assertEqual(article.text, "text")

    # def test_blank_data(self):
    #     form = ArticleForm()
    #     self.assertFalse(form.is_valid())
    #     self.assertEqual(form.errors, {
    #         'title': ['required'],
    #         'text': ['required'],
    #     })


class CommentFormTest(TestCase):
    def test_text_form(self):
        text = 'test_text'
        form_data = {'text': text}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())


class CommentModelTest(TestCase):
    def test_string_representation(self):
        comment = Comment(text="text")
        self.assertEqual(str(comment), "text")


class ArticleSerializerTest(TestCase):
    def setUp(self):

        self.register_user = {'username': 'testuser1', 'password': '12345'}
        self.user = User.objects.create_user(**self.register_user)

        self.article_attributes = {
            'author': self.user,
            'title': 'title_serializer',
            'text': 'text_serializer'
        }

        self.serializer_data = {
            'author': self.user,
            'title': 'title_serializer',
            'text': 'text_serializer'
        }
        self.article = Article.objects.create(**self.article_attributes)

    def test_contains_expected_fields(self):
        # print(self.article.id)
        serializer = ArticleSerializer(instance=self.article)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(
            ['id', 'pub_date', 'author', 'update', 'title', 'text'])
        )


