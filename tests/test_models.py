from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import Cook, Dish, DishType


class ModelsTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="Test1"
        )
        self.assertEqual(str(dish_type), dish_type.name)

    def test_cook_first_name_label(self):
        get_user_model().objects.create_user(
            username="test",
            password="1234test123",
            first_name="Pimp",
            last_name="Lazo"
        )
        field_label = Cook._meta.get_field("first_name").verbose_name
        self.assertEqual(field_label, "first name")

    def test_get_absolute_url(self):
        cook = get_user_model().objects.create_user(
            username="test",
            password="1234test123",
            first_name="Pimp",
            last_name="Lazo"
        )
        self.assertEqual(cook.get_absolute_url(), "/cooks/1/")

    def test_dish_str(self):
        dish_type = DishType.objects.create(
            name="Test1"
        )
        dish = Dish.objects.create(
            name="Potato",
            price=10.10,
            dish_type=dish_type
        )

        self.assertEqual(str(dish), f"{dish.name} (price: {dish.price}, type: {dish_type.name})")

    def test_create_cook_with_experience(self):
        username = "test"
        password = "test1234"
        years_of_experience = 4

        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience
        )

        self.assertEqual(cook.username, username)
        self.assertTrue(cook.check_password(password))
        self.assertEqual(cook.years_of_experience, years_of_experience)
