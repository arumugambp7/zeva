from django.contrib import admin
from .models import Category,Tutus,Customer,Follower

# Register your models here.
class CatAdmin(admin.ModelAdmin):
    list_display = ['title',]


class TutusAdmin(admin.ModelAdmin):
    list_display = ['name',]


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name',]


admin.site.register(Category, CatAdmin)
admin.site.register(Tutus, TutusAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Follower)
