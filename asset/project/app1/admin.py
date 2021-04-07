from django.contrib import admin

from .models import *

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    model = Book

    class Meta:
        fields = ("id", "title", "author")

admin.site.register(Book, BookAdmin)

class PersonAdmin(admin.ModelAdmin):
    model = Person

admin.site.register(Person, PersonAdmin)