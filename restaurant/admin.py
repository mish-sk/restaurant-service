from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from restaurant.models import Cook, Dish, DishType


@admin.register(Cook)
class CookAdmin(admin.ModelAdmin):
    list_display = UserAdmin.list_display


admin.register(Dish)
admin.register(DishType)
