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
         first_item = Skills()
         first_item.text = 'ghi'
         first_item.save()
         second_item = Skills()
         second_item.text = 'jkl'
         second_item.save()
         saved_items = Skills.objects.all()
         self.assertEqual(saved_items.count(), 2)
         first_saved_item = saved_items[0]
         second_saved_item = saved_items[1]
         self.assertEqual(first_saved_item.text, 'ghi)
         self.assertEqual(second_saved_item.text, 'jkl')
         first_item = Experience()
         first_item.text = 'mno'
         first_item.save()
         second_item = Experience()
         second_item.text = 'pqr'
         second_item.save()
         saved_items = Experience.objects.all()
         self.assertEqual(saved_items.count(), 2)
         first_saved_item = saved_items[0]
         second_saved_item = saved_items[1]
         self.assertEqual(first_saved_item.text, 'mno')
         self.assertEqual(second_saved_item.text, 'pqr')
         self.assertEquals(Experience.objects.first().date,'Present')




