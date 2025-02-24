from django.contrib import admin
from django.urls import path, include
from . import views  # استيراد وظائف العرض الخاصة بالمشروع الرئيسي

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # الصفحة الرئيسية
    path('comparisons/', include('comparisons.urls')),  # قسم مقارنة الأديان
    path('famous/', include('famous_preachers.urls')),  # قسم الدعاة المشاهير
    path('multilingual/', include('multilingual_preachers.urls')),  # قسم الدعاة بلغات أخرى
]