# -*- coding: utf-8 -*-
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from django.views.generic import View
from django.views.generic.base import (
    TemplateView,
    TemplateResponseMixin,
    ContextMixin,
)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)

from django.utils.decorators import method_decorator

from .models import Book
from .forms import BookForm


class BookCreate(CreateView):
    # model = Book
    # fields = ['title', 'description']

    template_name = 'dashboard/forms.html'
    form_class = BookForm

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        form.instance.last_edited_by = self.request.user
        return super(BookCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('dashboard:book_list')


class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'dashboard/forms.html'


class BookList(ListView):
    model = Book

    def get_queryset(self, *args, **kwargs):
        qs = super(BookList, self).get_queryset(*args, **kwargs)
        qs = qs.order_by('id')
        return qs


# from django.shortcuts import render

# def book_detail(request, slug):
#     books = Book.objects.get(slug=slug)
#     context = {'books', books}
#     return render(request, context)
# ↓ Same Way


class BookDetail(DetailView):
    model = Book

    def get_context_data(self, *args, **kwargs):
        context = super(DetailView, self).get_context_data(*args, **kwargs)

        return context


class LonginRequireMixin(object):
    # @classmethod
    # def as_view(cls, **kwargs):
    #     view = super(LonginRequireMixin, cls).as_view(**kwargs)
    #     return login_required(view)
    # ↓ Same Way
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LonginRequireMixin, self).dispatch(
            request, *args, **kwargs)


class DashboardTemplateView(LonginRequireMixin, TemplateView):
    template_name = 'newsletter/about.html'

    def get_context_data(self, *args, **kwargs):
        context = super(
            DashboardTemplateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'This is about us'
        return context
# ↓ Same Way


class MyView(ContextMixin, TemplateResponseMixin, View):
    template_name = 'newsletter/about.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['title'] = 'some other title'
        return self.render_to_response(context)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MyView, self).dispatch(request, *args, **kwargs)
