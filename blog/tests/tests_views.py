from django.test import TestCase,Client
from django.urls import reverse
from blog.models import Education,Experience,Skills,Contact,Workshops
import json


class TestViews(TestCase):
    def test_CV_contents_GET(self):
        c=Client()
        response=c.get(reverse('cv'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'/cv')
        