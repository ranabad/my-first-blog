from django.test import SimpleTestCase
from django.urls import reverse,resolve
from blog.views import EducationCV


class TestUrls(SimpleTestCase):
    def test_Education_url_is_resolved(self):
        url=reverse('cvEducation')
        print(resolve(url))
        self.assertEquals(resolve(url).func,EducationCV)