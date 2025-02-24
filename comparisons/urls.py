from django.urls import path
from . import views

urlpatterns = [
    path('', views.religion_list, name='religion_list'),  # صفحة قائمة الأديان
]