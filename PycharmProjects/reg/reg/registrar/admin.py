from django.contrib import admin

# Register your models here.
from registrar.models import *
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Professor)
