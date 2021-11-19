from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from portfolio import views
from .import views

app_name = 'blog'
urlpatterns = [
    
    path('',views.all_blogs,name = 'all_blogs'),
    path('<int:blog_id>/',views.detail,name = 'detail'),
    
]
