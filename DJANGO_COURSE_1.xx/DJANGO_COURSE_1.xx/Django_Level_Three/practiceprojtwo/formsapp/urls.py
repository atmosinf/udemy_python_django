from django.urls import re_path
from formsapp import views

urlpatterns = [
    re_path(r'^', views.form, name='form')
]
