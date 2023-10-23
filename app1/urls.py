from django.urls import path,include
from .views import *

urlpatterns = [
    path('f1',f1),
    path('vi',Auth.as_view({"post":"create"}))
]