from django.shortcuts import render
from onlineexam.models import Exam


def examonline(request):
    results=exam.objects.all()
    return render(request,'index.html', {"Exam":results})