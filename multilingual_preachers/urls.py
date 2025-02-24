from django.urls import path
from . import views

urlpatterns = [
    path('', views.multilingual_preacher_list, name='multilingual_preacher_list'),  # صفحة الدعاة بلغات أخرى
]