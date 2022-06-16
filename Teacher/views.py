from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from Teacher.models import Teacher
from .forms import TeacherAdd_Form
import json
from django.http import JsonResponse


def Teacher_detail(request):
    context = {}
    fm = TeacherAdd_Form()
    tchr_dtls = Teacher.objects.all()
    context = {'show':tchr_dtls,'teacher_add_form':fm}
    return render(request, 'Teacher_detail.html',context)

def teacher_add_sv(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax and request.method == "POST":
        fm = TeacherAdd_Form(request.POST)        
        if fm.is_valid():
            fm.save()
            return JsonResponse({"Sucess": True}, status=200)
        else:
            return JsonResponse({"error": fm.errors}, status=400)
            
    return JsonResponse({"error": ""}, status=400)
    

def teacher_profile(request,*args, **kwargs):
    tchr_id=kwargs.get('pk')
    print("P",tchr_id)
    context = {}
    tchr_dtls = Teacher.objects.get(id=tchr_id)
    context = {'show':tchr_dtls}
    return render(request, 'Teacher_Profile.html',context)







