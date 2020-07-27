from django.test import TestCase,Client
from django.urls import reverse
from blog.models import Education,Experience,Skills,Contact,Workshops
import json


class TestViews(TestCase):
    def setUp(self):
        self.client=Client()
        self.url_cv=reverse('cv')
    def test_CV_contents_GET(self):
        response=self.client.get(self.url_cv)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/cv.html')


        