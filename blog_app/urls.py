from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'blog-home'),
    path('about/',views.about, name = 'blog-about'),
]

#why we use trailing or forward slash in url?