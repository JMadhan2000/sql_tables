from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(dept)

admin.site.register(emp)

admin.site.register(bonus)

admin.site.register(salgrade)