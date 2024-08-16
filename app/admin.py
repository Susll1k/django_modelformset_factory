from django.contrib import admin
from .models import Recipe, Ingredients, Todo

admin.site.register(Recipe)
admin.site.register(Ingredients)
admin.site.register(Todo)

