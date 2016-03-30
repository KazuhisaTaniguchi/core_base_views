# -*- coding: utf-8 -*-
from django import forms
from .models import Book
from django.utils.text import slugify


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'description',
        ]

    def clean_title(self):
        title = self.cleaned_data.get('title')
        slug = slugify(title)
        try:
            book = Book.objects.get(slug=slug)
            raise forms.ValidationError(
                'そのタイトルでは､記事を追加できません｡',
            )
        except Book.DoesNotExist:
            return title
        except:
            raise forms.ValidationError(
                'そのタイトルでは､記事を追加できません｡',
            )
