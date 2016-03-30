from django.contrib import admin

from .forms import BookForm
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = [
        '__unicode__',
        'slug',
    ]
    readonly_fields = [
        'timestamp',
        'updated',
        'added_by',
        'last_edited_by',
    ]

    form = BookForm

admin.site.register(Book, BookAdmin)
