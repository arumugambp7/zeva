from django.contrib import admin
from .models import Menu,Collection,Client,Subscriber


# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title',]

admin.site.register(Menu, MenuAdmin)
admin.site.register(Collection)
admin.site.register(Client)
admin.site.register(Subscriber)
