from django.urls import path

from accountapp import views


app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', views.hello_world, name='hello_world '),
]
