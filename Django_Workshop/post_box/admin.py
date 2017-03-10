from django.contrib import admin
from .models import Person,Adress,Telephone,Email
# Register your models here.
admin.site.register([Person,Adress,Telephone,Email])