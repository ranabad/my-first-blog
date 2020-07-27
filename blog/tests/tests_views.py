from django.test import TestCase,Client
from django.urls import reverse
from blog.models import Education,Experience,Skills,Contact,Workshops
import json


class TestViews(TestCase):
    def setUp(self):
    
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.c = Client()
        logged_in = c.login(username='testuser', password='12345')
        self.assertTrue(logged_in) 
        self.url_cv=reverse('cv')
        self.url_edu=reverse('cvEducation')
        self.edu=Education.objects.create(text='abc',date='123')
    def test_CV_contents_GET(self):
        response=self.c.get(self.url_cv)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/cv.html')
    def test_CV_contents_with_POST(self):
        response=self.c.post(self.url_edu,{'text':'abc','date':'123'})
        self.assertEquals(response.status_code,302)
        #self.assertEquals(self.edu.first().text,'abc')
        #self.assertEqual(Education.objects.count(),1)
        print(response.content)


        