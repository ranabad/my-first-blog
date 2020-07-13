from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from blog.views import InteractiveCV
from blog.models import Education
from django.utils import timezone
from django.urls import reverse


class CVPageTest(TestCase):

     def test_uses_CV_template(self):
         response = self.client.get('/cv')
         self.assertTemplateUsed(response, 'blog/cv.html')

     def test_can_save_a_POST_request(self):
         self.client.post('/cv', data={'item_text': 'A new list item', 'date':timezone.now})
         new_item = Education.objects.first()
         self.assertEqual(Education.objects.count(),0)
         


     def test_redirects_after_POST(self):
         response = self.client.post('/cv', data={'item_text': 'A new list item'})
         self.assertEqual(response.status_code, 302)
         self.assertEqual(response['location'], '/cv')

     def test_only_saves_items_when_necessary(self):
         self.client.get('/cv')
         self.assertEqual(Education.objects.count(), 0)

     def test_displays_all_list_items(self):
         Education.objects.create(text='itemey 1')
         Education.objects.create(text='itemey 2')

         response = self.client.get('/cv')

         self.assertIn('itemey 1', response.content.decode())
         self.assertIn('itemey 2', response.content.decode())

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
