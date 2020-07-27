from django.test import SimpleTestCase
from django.urls import resolve, reverse

from blog.views import (CV, ContactCV, ContactCVMsg, EducationCV,
                        EducationCVDlt, EducationCVUpdatde, ExperienceCV,
                        ExperienceCVDlt, ExperienceCVUpdatde, SkillsCV,
                        SkillsCVDlt, SkillsCVUpdatde, WorkshopsCV,
                        WorkshopsCVDlt, WorkshopsCVUpdatde, msg_remove)


class TestUrls(SimpleTestCase):
    def test_cv_edu_skills_workshop_exp_con_msg_url_is_resolved(self):
        url_skill=reverse('cvSkills')
        url_main=reverse('cv')
        url_workshop=reverse('cvWorkshop')
        url_exp=reverse('cvExperience')
        url_edu=reverse('cvEducation')
        url_con=reverse('contact')
        url_msg=reverse('msg')
        self.assertEquals(resolve(url_edu).func,EducationCV)
        self.assertEquals(resolve(url_con).func,ContactCV)
        self.assertEquals(resolve(url_msg).func,ContactCVMsg)
        self.assertEquals(resolve(url_exp).func,ExperienceCV)
        self.assertEquals(resolve(url_main).func,CV)
        self.assertEquals(resolve(url_skill).func,SkillsCV)
        self.assertEquals(resolve(url_workshop).func,WorkshopsCV)
    def test_edu_skills_workshop_exp_update_url_is_resolved(self):
        url_skill=reverse('cv_Skills_edit',args=[1])
        url_workshop=reverse('cv_Workshop_edit',args=[1])
        url_exp=reverse('cv_Experience_edit',args=[1])
        url_edu=reverse('cv_Education_edit',args=[1])
        self.assertEquals(resolve(url_skill).func,SkillsCVUpdatde)
        self.assertEquals(resolve(url_workshop).func,WorkshopsCVUpdatde)
        self.assertEquals(resolve(url_exp).func,ExperienceCVUpdatde)
        self.assertEquals(resolve(url_edu).func,EducationCVUpdatde)
    def test_edu_skills_workshop_exp_msg_dlt_url_is_resolved(self):
        url_skill=reverse('cv_Skills_dlt',args=[1])
        url_workshop=reverse('cv_Workshop_dlt',args=[1])
        url_exp=reverse('cv_Experience_dlt',args=[1])
        url_edu=reverse('cv_Education_dlt',args=[1])
        url_msg=reverse('msg_remove',args=[1])
        self.assertEquals(resolve(url_msg).func,msg_remove)
        self.assertEquals(resolve(url_skill).func,SkillsCVDlt)
        self.assertEquals(resolve(url_workshop).func,WorkshopsCVDlt)
        self.assertEquals(resolve(url_exp).func,ExperienceCVDlt)
        self.assertEquals(resolve(url_edu).func,EducationCVDlt)
           
 
 

   
