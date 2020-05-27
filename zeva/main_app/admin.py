from django.contrib import admin
from .models import Menu,Collection,Customer,Follower

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title',]


class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name',]


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name',]


class FollowerAdmin(admin.ModelAdmin):
    list_display = ['name',]


admin.site.register(Menu, MenuAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Follower, FollowerAdmin)
