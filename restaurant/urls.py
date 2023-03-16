from django.urls import path

from .views import (
    index,
    CookListView, CookDetailView, DishViewList,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "cooks/",
        CookListView.as_view(),
        name="cook-list",
    ),
    path(
        "cooks/<int:pk>/",
        CookDetailView.as_view(),
        name="cook-detail",
    ),
    path(
        "dishes/",
        DishViewList.as_view(),
        name="dish-list",
    ),
]

app_name = "restaurant"
