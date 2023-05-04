from django.test import TestCase

from kitchen.forms import CookCreationForm


class FormsTests(TestCase):
    def test_cook_creation_form_with_all_data_is_valid(self):
        form_data = {
            "username": "test1",
            "password1": "1qazcde3",
            "password2": "1qazcde3",
            "first_name": "test first",
            "last_name": "test last",
            "years_of_experience": 4
        }

        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
