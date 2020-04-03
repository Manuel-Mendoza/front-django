from django.contrib import admin
from django.urls import path
from .vista import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('register/', register, name="register"),
    path('support/', support, name="support"),
]
