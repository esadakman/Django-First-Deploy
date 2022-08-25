from django.contrib import admin

from courses.models import Category
from .models import Category, Courses
# Register your models here.
admin.site.register(Category)
admin.site.register(Courses)
