from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from blog.views import InteractiveCV


class CVPageTest(TestCase):

    def test_uses_CV_template(self):
        response = self.client.get('/cv')
        self.assertTemplateUsed(response, 'blog/InteractiveCv/cv.html')