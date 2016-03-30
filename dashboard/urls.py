# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import (
    BookDetail,
    BookList,
    BookCreate,
    BookUpdate,
)

urlpatterns = [
    url(r'^book/$', BookList.as_view(), name='book_list'),
    url(r'^book/create/$', BookCreate.as_view(), name='book_create'),
    url(r'^book/update/(?P<slug>[-\w]+)/$',
        BookUpdate.as_view(), name='book_update'),
    url(r'^book/(?P<slug>[-\w]+)/$', BookDetail.as_view(), name='book_detail'),
]
