from django.contrib import admin
from .models import AvtorModel, BookModel

class AvtorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'about', 'birthday', 'country')

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'page', 'price', 'year', 'avtor')

admin.site.register(AvtorModel, AvtorAdmin)
admin.site.register(BookModel, BookAdmin)