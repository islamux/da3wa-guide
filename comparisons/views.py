from django.shortcuts import render
from .models import Religion

def religion_list(request):
    religions = Religion.objects.all()  # استرجاع جميع الأديان من قاعدة البيانات
    return render(request, 'comparisons/religion_list.html', {'religions': religions})