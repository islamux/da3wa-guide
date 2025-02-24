from django.shortcuts import render
from .models import FamousPreacher

def preacher_list(request):
    preachers = FamousPreacher.objects.all()  # استرجاع جميع الدعاة المشاهير
    return render(request, 'famous_preachers/preacher_list.html', {'preachers': preachers})