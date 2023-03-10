from django.shortcuts import render
from django.http import HttpResponse
from .models import Bb
from.models import Rubric 

def index(request):
    s = 'Список обьявлений\r\n\r\n\r\n'
    for bb in Bb.objects.order_by('-published'):
        s += Bb.title + '\r\n' + bb.content + '\r\n'
    return HttpResponse(s, content_type = 'text/plain, charset=utf-8')

def by_rubric(reqrest, rubric_id):
    bbs = Bb.objects.filter(rubric = rubric_id)
    rubrics = rubric.objects.all()
    current_rubric = Rubric.odjects.get(pk = rubric_id)
    context = {
        "bbs": bbs, 
        "rubrics": rubrics, 
        "current_rubric": current_rubric
        
    }   

    return render(request, "bboard/by_rubric.html", context)
