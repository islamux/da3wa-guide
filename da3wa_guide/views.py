from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # عرض الصفحة الرئيسية