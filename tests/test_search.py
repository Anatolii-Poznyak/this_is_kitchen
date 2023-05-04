from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Dish, DishType

DISH_TYPE_LIST_URL = reverse("kitchen:dish-type-list")
COOK_LIST_URL = reverse("kitchen:cook-list")
DISH_LIST_URL = reverse("kitchen:dish-list")


class SearchFeatureTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password123"
        )
        self.client.force_login(self.user)

        self.cook1 = get_user_model().objects.create_user(
            username="test1",
            password="1234test123",
            first_name="Pimp1",
            last_name="Lazo1",
            years_of_experience=2
        )
        self.cook2 = get_user_model().objects.create_user(
            username="test2",
            password="1234test123",
            first_name="Pimp2",
            last_name="Lazo2",
            years_of_experience=3
        )
        self.cook3 = get_user_model().objects.create_user(
            username="Giovanni",
            password="1234test123",
            first_name="Joe",
            last_name="Bobotto"
        )
        self.dish_type1 = DishType.objects.create(
            name="Test1"
        )
        self.dish_type2 = DishType.objects.create(
            name="Test2"
        )
        self.dish1 = Dish.objects.create(
            name="TestModel1",
            price=12.20,
            dish_type=self.dish_type1
        )
        self.dish2 = Dish.objects.create(
            name="TestModel2",
            price=13.20,
            dish_type=self.dish_type2
        )

    def test_empty_search_form(self):
        res = self.client.get(DISH_LIST_URL, {"title": ""})

        self.assertContains(res, self.dish1.name)
        self.assertContains(res, self.dish2.price)

    def test_success_search_with_partly_match(self):
        res = self.client.get(COOK_LIST_URL, {"title": "est"})

        self.assertContains(res, self.cook1.first_name)
        self.assertContains(res, self.cook2.last_name)
        self.assertNotContains(res, self.cook3)

    def test_search_with_absent_car(self):
        res = self.client.get(DISH_LIST_URL, {"title": "Tesla"})

        self.assertNotContains(res, self.dish1)
        self.assertNotContains(res, self.dish2)
