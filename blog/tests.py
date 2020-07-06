from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from blog.views import InteractiveCV
from blog.models import Item


class CVPageTest(TestCase):

    def test_uses_CV_template(self):
        response = self.client.get('/cv')
        self.assertTemplateUsed(response, 'blog/InteractiveCV/cv.html')

    def test_can_save_a_POST_request(self):
        self.client.post('/cv', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')


    def test_redirects_after_POST(self):
        response = self.client.post('/cv', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/cv')
        self.assertEqual(Item.objects.count(), 0)

    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/cv')

        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')     
