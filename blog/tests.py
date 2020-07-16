from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve, reverse
from django.utils import timezone

from blog.forms import EducationForm,SkillsForm
from blog.models import Education,Skills
from blog.views import EducationCV,SkillsCV
from django.http import HttpResponse


class CVEducationiewsTest(TestCase):

     def test_uses_CV_template(self):
         response = self.client.get('/cv/Education')
         self.assertTemplateUsed(response, 'blog/cvEducation.html')

     def test_can_save_a_POST_request_in_Education(self):
         self.client.post('/cv/Education', data={'item_text': 'A new list item', 'date':timezone.now})
         new_item = Education.objects.first()
         self.assertEqual(Education.objects.count(),0)
     def test_redirects_after_POST_in_Education(self):
         response = self.client.post('/cv/Education', data={'item_text': 'A new list item'})
         self.assertEqual(response.status_code, 302)
         self.assertEqual(response['location'], '/cv/Education')
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
from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve, reverse
from django.utils import timezone

from blog.forms import SkillsForm
from blog.models import Skills
from blog.views import SkillsCV
from django.http import HttpResponse


class CVSkillsiewsTest(TestCase):

     def test_uses_CV_template(self):
         response = self.client.get('/cv/Skills')
         self.assertTemplateUsed(response, 'blog/cvSkills.html')

     def test_can_save_a_POST_request_in_Skills(self):
         self.client.post('/cv/Skills', data={'item_text': 'A new list item', 'date':timezone.now})
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
         self.client.post('/cv/1/edit/', data={'item_text': 'Hello', 'date':timezone.now})
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


