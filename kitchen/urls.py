from django.urls import path

from kitchen.views import (index,
                           DishTypeListView,
                           DishTypeCreateView,
                           DishListView,
                           DishDetailView,
                           CookListView,
                           CookDetailView,
                           CookCreateView)




urlpatterns = [
    path("", index, name="index"),
    path(
        "dish-types/",
        DishTypeListView.as_view(),
        name="dish-type-list"
    ),
    path(
        "dish-types/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create"
    ),
    path(
        "dishes/",
        DishListView.as_view(),
        name="dish-list"
    ),
    path(
        "dishes/<int:pk>/",
        DishDetailView.as_view(),
        name="dish-detail"
    ),
    path(
        "cooks/",
        CookListView.as_view(),
        name="cook-list"
    ),
    path(
        "cooks/<int:pk>/",
        CookDetailView.as_view(),
        name="cook-detail"
    ),
    path(
        "cooks/create/",
        CookCreateView.as_view(),
        name="cook-create"
    ),

]

app_name = "kitchen"
