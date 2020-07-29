from django.test import SimpleTestCase

from blog.forms import (ContactForm, EducationForm, ExperienceForm, SkillsForm,
                        WorkshopsForm)


class testForms(SimpleTestCase):

    def test_form_valid_data(self):
        form=ContactForm(data={'from_email':'123@gmail.com','from_name':'tester','subject':'modeltest','message':'testing forms now'})
        self.assertTrue(form.is_valid())