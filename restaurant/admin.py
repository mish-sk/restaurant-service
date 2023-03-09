from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from restaurant.models import Cook, Dish, DishType


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("dish_type",)


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    search_fields = ("name",)
