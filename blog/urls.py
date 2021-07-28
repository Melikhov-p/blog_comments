from django.contrib import admin
from django.urls import path
from blog.views import *

urlpatterns = [
    path('', blog, name='blog'),
    path('create/', create_article, name='create_article')
]