from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from blog.views import InteractiveCV


class CVPageTest(TestCase):

    def test_uses_CV_template(self):
        response = self.client.get('/cv')
        self.assertTemplateUsed(response, 'blog/InteractiveCv/cv.html')

    def test_can_save_a_POST_request(self):
    response = self.client.post('/cv', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'blog/InteractiveCv/cv.html')
     