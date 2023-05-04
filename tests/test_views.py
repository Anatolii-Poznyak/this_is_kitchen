from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import DishType

DISH_TYPE_LIST_URL = reverse("kitchen:dish-type-list")


class PublicDishTypeTests(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_TYPE_LIST_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateDishTypeTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password123"
        )
        self.client.force_login(self.user)

    def test_access_dish_types(self):
        DishType.objects.create(name="ABC")
        DishType.objects.create(name="CBA")

        res = self.client.get(DISH_TYPE_LIST_URL)

        dish_types = DishType.objects.all()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context["dish_type_list"]),
            list(dish_types)
        )
        self.assertTemplateUsed(res, "kitchen/dish_type_list.html")


class PrivateCookTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "test",
            "password123"
        )

        self.client.force_login(self.user)

    def test_create_cook(self):
        form_data = {
            "username": "test1",
            "password1": "1qazcde3",
            "password2": "1qazcde3",
            "first_name": "test first",
            "last_name": "test last",
            "years_of_experience": 5
        }

        self.client.post(reverse("kitchen:cook-create"), data=form_data)
        user_created = get_user_model().objects.get(
            username=form_data["username"]
        )
        self.assertEqual(user_created.first_name,
                         form_data["first_name"])
        self.assertEqual(user_created.years_of_experience,
                         form_data["years_of_experience"])
        self.assertEqual(user_created.last_name,
                         form_data["last_name"])
