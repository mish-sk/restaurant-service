from typing import Any, List

from django.shortcuts import render
from django.views import generic

from restaurant.models import Cook, Dish, DishType


def index(request):
    """View function for the home page of the site."""
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
    }

    return render(request, "restaurant/index.html", context=context)


class CookListView(generic.ListView):
    model = Cook
    # paginate_by = 3


class CookDetailView(generic.DetailView):
    model = Cook
    queryset = Cook.objects.prefetch_related("dishes__dish_type")


class DishViewList(generic.ListView):
    model = Dish

