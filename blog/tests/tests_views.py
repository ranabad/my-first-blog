import json

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from blog.models import Contact, Education, Experience, Skills, Workshops


class TestViews(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.c = Client()
        logged_in =self.c.login(username='testuser', password='12345')
        self.assertTrue(logged_in) 
        self.url_cv=reverse('cv')
        self.url_edu=reverse('cvEducation')  
        self.url_skill=reverse('cvSkills')
        self.url_workshop=reverse('cvWorkshop')
        self.url_exp=reverse('cvExperience')
        self.url_con=reverse('contact')
        self.url_msg=reverse('msg')
        self.url_skillUp=reverse('cv_Skills_edit',args=[1])
        self.url_workshopUp=reverse('cv_Workshop_edit',args=[1])
        self.url_expUp=reverse('cv_Experience_edit',args=[1])
        self.url_eduUp=reverse('cv_Education_edit',args=[1])
        self.url_skillDlt=reverse('cv_Skills_dlt',args=[1])
        self.url_workshopDlt=reverse('cv_Workshop_dlt',args=[1])
        self.url_expDlt=reverse('cv_Experience_dlt',args=[1])
        self.url_eduDlt=reverse('cv_Education_dlt',args=[1])
        self.url_msgDlt=reverse('msg_remove',args=[1])
    def test_CV_contents_GET(self):
        response=self.c.get(self.url_cv)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/cv.html')
        response=self.c.get(self.url_edu)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/cvEducation.html')
        response=self.c.get(self.url_skill)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/cvSkill.html')
        response=self.c.get(self.url_workshop)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/cvWorkshop.html')
        response=self.c.get(self.url_exp)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/cvExperince.html')
        response=self.c.get(self.url_con)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/cvContactForm.html')
        response=self.c.get(self.url_msg)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/cvContactMsg.html')
        response=self.c.get(self.url_eduUp)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/cvEducationUpdate.html')
        response=self.c.get(self.url_skillUp)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/cvSkillUpdate.html')
        response=self.c.get(self.url_workshopUp)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/cvWorkshopsUpdate.html')
        response=self.c.get(self.url_expUp)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/cvExperinceUpdate.html')
        response=self.c.get(self.url_eduDlt)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/cvEducationDlt.html')
        response=self.c.get(self.url_skillDlt)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/cvSkillDlt.html')
        response=self.c.get(self.url_workshopDlt)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/cvWorkshopDlt.html')
        response=self.c.get(self.url_expDlt)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/cvExperinceDlt.html')
    def test_CV_contents_with_POST(self):
        posting=self.c.post(self.url_edu,data={'text':'abc','date':'123'})
        self.assertEquals(posting.status_code,302)
        self.assertEqual(Education.objects.count(),1)
        response = self.client.get('/cv')
        self.assertIn('abc', response.content.decode())
        
        
        


        
