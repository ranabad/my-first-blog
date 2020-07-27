from django.test import SimpleTestCase
from django.urls import reverse,resolve
from blog.views import EducationCV,CV,SkillsCV,WorkshopsCV,ExperienceCV,ContactCV,ContactCVMsg


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
        self.assertEquals(resolve(url_skill).func,SkillsCVUpdatde)


        

    

          
    
    
