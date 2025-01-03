from django.contrib import admin
from .models import Teachers,Group,Stiuation,Students,Appartment

admin.site.register(Stiuation)
admin.site.register(Students)
admin.site.register(Teachers)
admin.site.register(Group)
admin.site.register(Appartment)