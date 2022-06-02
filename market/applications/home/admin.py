from django.contrib import admin

from .models import Contact, Meet, Group
# Register your models here.

admin.site.register(Contact),
admin.site.register(Meet),
admin.site.register(Group),

