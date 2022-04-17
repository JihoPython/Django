from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
