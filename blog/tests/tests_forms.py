from django.test import SimpleTestCase

from blog.forms import (ContactForm, EducationForm, ExperienceForm, SkillsForm,
                        WorkshopsForm)


class testForms(SimpleTestCase):

    def test_form_valid_data(self):
        form=ContactForm(data={'from_email':'123@gmail.com','from_name':'tester','subject':'modeltest','message':'testing forms now'})
        self.assertTrue(form.is_valid())
        form=EducationForm(data={'text':'abc','date':'123'})
        self.assertTrue(form.is_valid())
        form=ExperienceForm(data={'text':'abc','date':'123'})
        self.assertTrue(form.is_valid())
        form=WorkshopsForm(data={'text':'abc','date':'123'})
        self.assertTrue(form.is_valid())
        form=EducationForm(data={'text':'abc'})
        self.assertTrue(form.is_valid())
