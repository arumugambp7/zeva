from django.contrib import admin
from .models import Menu,Collection,Client,Subscriber

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title',]


class CollAdmin(admin.ModelAdmin):
    list_display = ['name',]


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name',]


admin.site.register(Menu, MenuAdmin)
admin.site.register(Collection, CollAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Subscriber)
