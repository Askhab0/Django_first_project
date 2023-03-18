from django.urls import path
from django.http import HttpResponse

from dashboard.views import index

urlpatterns = [
    path('', index, name='index')
]