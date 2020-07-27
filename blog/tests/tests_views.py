from django.test import TestCase,Client
from django.urls import reverse
from blog.models import Education,Experience,Skills,Contact,Workshops
import json


class TestViews(TestCase):
    def setUp(self):
        self.client=Client()
        self.url_cv=reverse('cv')
        self.url_edu=reverse('cvEducation')
        self.edu=Education.objects.create(text='abc',date='123')
    def test_CV_contents_GET(self):
        response=self.client.get(self.url_cv)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/cv.html')
    def test_CV_contents_with_POST(self):
        response=self.client.post(self.url_edu,{'text':'abc','date':'123'})
        self.assertEquals(response.status_code,302)
        self.assertEquals(self.edu.first().text,'abc')

        