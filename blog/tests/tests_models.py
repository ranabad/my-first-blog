from django.test import TestCase

from blog.models import Contact, Education, Experience, Skills, Workshops


class ModelTest(TestCase):
     def test_saving_and_retrieving_items(self):
         first_item = Education()
         first_item.text = 'abc'
         first_item.date='123'
         first_item.save()
         second_item = Education()
         second_item.text = 'def'
         first_item.date='456'
         second_item.save()
         saved_items = Education.objects.all()
         self.assertEqual(saved_items.count(), 2)
         first_saved_item = saved_items[0]
         second_saved_item = saved_items[1]
         self.assertEqual(first_saved_item.text, 'abc')
         self.assertEqual(second_saved_item.text, 'def') 
