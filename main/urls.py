from django.contrib import admin
from django.urls import path
from main.views import index, time_plus, hours_ahead

urlpatterns = [
    path('', index),
    path('time/plus/', time_plus),
    path('time/plus/<int:{hours}>/<int:{days}>/'.format(hours='asd', days='asd1'), hours_ahead),
]