from django.urls import re_path
from basicapp import views

urlpatterns = [
    re_path(r'^form/', views.form, name='form')
]
