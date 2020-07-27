from django.test import SimpleTestCase
from danjgo.urls import reverse,resolve
from blog.views import EducationCV


class TestUrls(SimpleTestCase):
    def test_Education_url_is_resolved(self):
        path('cv/Education', views.EducationCV, name='cvEducation'),
        url=reverse('cvEducation')
        print(resolve(url))
