from django.shortcuts import render
from .models import MultilingualPreacher

def multilingual_preacher_list(request):
    preachers = MultilingualPreacher.objects.all()  # استرجاع الدعاة بلغات أخرى
    return render(request, 'multilingual_preachers/multilingual_preacher_list.html', {'preachers': preachers})