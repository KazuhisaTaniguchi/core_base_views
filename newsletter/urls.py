from django.conf.urls import url
from . import views
from dashboard.views import (
    DashboardTemplateView,
    MyView,
)

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^someview/$', MyView.as_view(), name='someview'),
    url(r'^about/$', DashboardTemplateView.as_view(), name='about'),
]
