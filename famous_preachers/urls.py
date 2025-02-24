from django.urls import path
from . import views

urlpatterns = [
    path('', views.preacher_list, name='preacher_list'),  # صفحة قائمة الدعاة المشاهير
]