from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.test import Client, TestCase
from django.urls import resolve, reverse
from django.utils import timezone

from blog.forms import EducationForm, ExperienceForm, SkillsForm, WorkshopsForm
from blog.models import Education, Experience, Skills, Workshops
from blog.views import CV, EducationCV, ExperienceCV, SkillsCV, WorkshopsCV,EducationCVUpdatde


class CVTestView(TestCase):
     def test_uses_CV_template(self):
         response = self.client.get('/cv')
         self.assertTemplateUsed(response, 'blog/cv.html')

class CVEducationTest(TestCase):

     def test_uses_CV_template2(self):
         response = self.client.get('/cv/Education')
         self.assertTemplateUsed(response, 'blog/cvEducation.html')
         user = User.objects.create(username='testuser')
         user.set_password('12345')
         user.save()
         c = Client()
         logged_in = c.login(username='testuser', password='12345')
         self.assertTrue(logged_in) 
         posting=c.post('/cv/Education',{'text':'Cheddar Talk', 'date':'Thoughts on cheese.'})
         posting.status_code
         self.assertEqual(posting.status_code, 302)
         self.assertEqual(posting['location'], '/cv/Education')
         self.assertEqual(Education.objects.count(),1)
         posting=c.get('cv/<1:pk>/Education/edit/')
         self.assertEqual(posting.status_code, 302)
         self.assertEqual(posting['location'], '/cv/1/Education/edit')
         posting.status_code
         posting=c.get('/cv')
         print(posting.content)
         #self.assertEqual(new_club.date, "FAIL")
         
         
        
        


   
     def test_only_saves_items_when_necessary(self):
         self.client.get('/cv/Education')
         self.assertEqual(Education.objects.count(), 0)
     def test_displays_all_list_items_in_Education(self):
         Education.objects.create(text='itemey 1')
         Education.objects.create(text='itemey 2')
         response = self.client.get('/cv')

         self.assertIn('itemey 1', response.content.decode())
         self.assertIn('itemey 2', response.content.decode())
     def test_Updates_selected_item_in_Education(self): 
         item=Education.objects.create(text='itemey 1')
         response = self.client.get('/cv')
         self.assertIn('itemey 1', response.content.decode())
         self.client.post('/cv/1/edit/', data={'item_text': 'Hello', 'date':timezone.now})
         new_item = Education.objects.first()
         self.assertEqual(Education.objects.count(),1)
     def test_dlts_selected_item_inEducation(self): 
         Education.objects.create(text='itemey 1')
         Education.objects.create(text='itemey 2')
         response = self.client.get('/cv')
         self.assertIn('itemey 1', response.content.decode())
         self.assertIn('itemey 2', response.content.decode())
         Education.objects.first().delete()
         self.assertEqual(Education.objects.count(), 1)

class EducationModelTest(TestCase):
     def test_saving_and_retrieving_items(self):
         first_item = Education()
         first_item.text = 'The first (ever) list item'
         first_item.save()

         second_item = Education()
         second_item.text = 'Item the second'
         second_item.save()

         saved_items = Education.objects.all()
         self.assertEqual(saved_items.count(), 2)

         first_saved_item = saved_items[0]
         second_saved_item = saved_items[1]
         self.assertEqual(first_saved_item.text, 'The first (ever) list item')
         self.assertEqual(second_saved_item.text, 'Item the second') 
class EducationFormTest(TestCase):     
        def test_form_item_input_has_placeholder_and_css_classes(self):
            form = EducationForm()
            self.assertIn('for="id_text"', form.as_p())
            self.assertIn('for="id_date"', form.as_p()) 

 

class CVSkillsiewsTest(TestCase):

     def test_uses_CV_template(self):
         response = self.client.get('/cv/Skills')
         self.assertTemplateUsed(response, 'blog/cvSkills.html')

     def test_can_save_a_POST_request_in_Skills(self):
         self.client.post('/cv/Skills', data={'item_text': 'A new list item', })
         new_item = Skills.objects.first()
         self.assertEqual(Skills.objects.count(),0)
     def test_redirects_after_POST_in_Skills(self):
         response = self.client.post('/cv/Skills', data={'item_text': 'A new list item'})
         self.assertEqual(response.status_code, 302)
         self.assertEqual(response['location'], '/cv/Skills')
     def test_only_saves_items_when_necessary(self):
         self.client.get('/cv/Skills')
         self.assertEqual(Skills.objects.count(), 0)
     def test_displays_all_list_items_in_Skills(self):
         Skills.objects.create(text='itemey 1')
         Skills.objects.create(text='itemey 2')
         response = self.client.get('/cv')

         self.assertIn('itemey 1', response.content.decode())
         self.assertIn('itemey 2', response.content.decode())
     def test_Updates_selected_item_in_Skills(self): 
         item=Skills.objects.create(text='itemey 1')
         response = self.client.get('/cv')
         self.assertIn('itemey 1', response.content.decode())
         self.client.post('/cv/1/edit/', data={'item_text': 'Hello', })
         new_item = Skills.objects.first()
         self.assertEqual(Skills.objects.count(),1)
     def test_dlts_selected_item_inSkills(self): 
         Skills.objects.create(text='itemey 1')
         Skills.objects.create(text='itemey 2')
         response = self.client.get('/cv')
         self.assertIn('itemey 1', response.content.decode())
         self.assertIn('itemey 2', response.content.decode())
         Skills.objects.first().delete()
         self.assertEqual(Skills.objects.count(), 1)

class SkillsModelTest(TestCase):
     def test_saving_and_retrieving_items(self):
         first_item = Skills()
         first_item.text = 'The first (ever) list item'
         first_item.save()

         second_item = Skills()
         second_item.text = 'Item the second'
         second_item.save()

         saved_items = Skills.objects.all()
         self.assertEqual(saved_items.count(), 2)

         first_saved_item = saved_items[0]
         second_saved_item = saved_items[1]
         self.assertEqual(first_saved_item.text, 'The first (ever) list item')
         self.assertEqual(second_saved_item.text, 'Item the second') 
class SkillsFormTest(TestCase):     
        def test_form_item_input_has_placeholder_and_css_classes(self):
            form = SkillsForm()
            self.assertIn('for="id_text"', form.as_p())
class CVWorkshopiewsTest(TestCase):

     def test_uses_CV_template(self):
         response = self.client.get('/cv/Workshop')
         self.assertTemplateUsed(response, 'blog/cvWorkshop.html')

     def test_can_save_a_POST_request_in_Workshop(self):
         self.client.post('/cv/Workshop', data={'item_text': 'A new list item', 'date':'Present',})
         new_item = Workshops.objects.first()
         self.assertEqual(Workshops.objects.count(),0)
     def test_redirects_after_POST_in_Workshop(self):
         response = self.client.post('/cv/Workshop', data={'item_text': 'A new list item'})
         self.assertEqual(response.status_code, 302)
         self.assertEqual(response['location'], '/cv/Workshop')
     def test_only_saves_items_when_necessary(self):
         self.client.get('/cv/Workshop')
         self.assertEqual(Workshops.objects.count(), 0)
     def test_displays_all_list_items_in_Workshop(self):
         Workshops.objects.create(text='itemey 1')
         Workshops.objects.create(text='itemey 2')
         response = self.client.get('/cv')

         self.assertIn('itemey 1', response.content.decode())
         self.assertIn('itemey 2', response.content.decode())
     def test_Updates_selected_item_in_Workshop(self): 
         item=Workshops.objects.create(text='itemey 1')
         response = self.client.get('/cv')
         self.assertIn('itemey 1', response.content.decode())
         self.client.post('/cv/1/edit/', data={'item_text': 'Hello', 'date':timezone.now})
         new_item = Workshops.objects.first()
         self.assertEqual(Workshops.objects.count(),1)
     def test_dlts_selected_item_inWorkshop(self): 
         Workshops.objects.create(text='itemey 1')
         Workshops.objects.create(text='itemey 2')
         response = self.client.get('/cv')
         self.assertIn('itemey 1', response.content.decode())
         self.assertIn('itemey 2', response.content.decode())
         Workshops.objects.first().delete()
         self.assertEqual(Workshops.objects.count(), 1)

class CVExperienceiewsTest(TestCase):

     def test_uses_CV_template(self):
         response = self.client.get('/cv/Experience')
         self.assertTemplateUsed(response, 'blog/cvExperience.html')

     def test_can_save_a_POST_request_in_Experience(self):
         self.client.post('/cv/Experience', data={'item_text': 'A new list item', 'date':'Present','grade':'Not applicable'})
         new_item = Experience.objects.first()
         self.assertEqual(Experience.objects.count(),0)
     def test_redirects_after_POST_in_Experience(self):
         response = self.client.post('/cv/Experience', data={'item_text': 'A new list item'})
         self.assertEqual(response.status_code, 302)
         self.assertEqual(response['location'], '/cv/Experience')
     def test_only_saves_items_when_necessary(self):
         self.client.get('/cv/Experience')
         self.assertEqual(Experience.objects.count(), 0)
     def test_displays_all_list_items_in_Experience(self):
         Experience.objects.create(text='itemey 1')
         Experience.objects.create(text='itemey 2')
         response = self.client.get('/cv')

         self.assertIn('itemey 1', response.content.decode())
         self.assertIn('itemey 2', response.content.decode())
     def test_Updates_selected_item_in_Experience(self): 
         item=Experience.objects.create(text='itemey 1')
         response = self.client.get('/cv')
         self.assertIn('itemey 1', response.content.decode())
         self.client.post('/cv/1/edit/', data={'item_text': 'Hello', 'date':timezone.now})
         new_item = Experience.objects.first()
         self.assertEqual(Experience.objects.count(),1)
     def test_dlts_selected_item_inExperience(self): 
         Experience.objects.create(text='itemey 1')
         Experience.objects.create(text='itemey 2')
         response = self.client.get('/cv')
         self.assertIn('itemey 1', response.content.decode())
         self.assertIn('itemey 2', response.content.decode())
         Experience.objects.first().delete()
         self.assertEqual(Experience.objects.count(), 1)

class ExperienceModelTest(TestCase):
     def test_saving_and_retrieving_items(self):
         first_item = Experience()
         first_item.text = 'The first (ever) list item'
         first_item.save()

         second_item = Experience()
         second_item.text = 'Item the second'
         second_item.save()

         saved_items = Experience.objects.all()
         self.assertEqual(saved_items.count(), 2)

         first_saved_item = saved_items[0]
         second_saved_item = saved_items[1]
         self.assertEqual(first_saved_item.text, 'The first (ever) list item')
         self.assertEqual(second_saved_item.text, 'Item the second') 
class ExperienceFormTest(TestCase):     
        def test_form_item_input_has_placeholder_and_css_classes(self):
            form = ExperienceForm()
            self.assertIn('for="id_text"', form.as_p())
            self.assertIn('for="id_date"', form.as_p()) 
class WorkshopModelTest(TestCase):
     def test_saving_and_retrieving_items(self):
         first_item = Workshops()
         first_item.text = 'The first (ever) list item'
         first_item.save()

         second_item = Workshops()
         second_item.text = 'Item the second'
         second_item.save()

         saved_items = Workshops.objects.all()
         self.assertEqual(saved_items.count(), 2)

         first_saved_item = saved_items[0]
         second_saved_item = saved_items[1]
         self.assertEqual(first_saved_item.text, 'The first (ever) list item')
         self.assertEqual(second_saved_item.text, 'Item the second') 
class WorkshopFormTest(TestCase):     
        def test_form_item_input_has_placeholder_and_css_classes(self):
            form = WorkshopsForm()
            self.assertIn('for="id_text"', form.as_p())
            self.assertIn('for="id_date"', form.as_p()) 


  
         