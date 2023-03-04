from django.shortcuts import render
from .models import *

def home(request):
    context = {
        "info": Info.objects.last(),
        'logo' : logo.objects.last(),
        'view' : View.objects.last() ,
        'project_text' : Project_text.objects.last(),
        'project' : Project.objects.all(),
        'about' : About.objects.last(),
        'suppor' : Suppor.objects.all().order_by('-id')[:4],
        'frequently' : Frequently.objects.all().order_by,
        'frequently_text': Frequently_text.objects.last(),
        'communyte' : Communyte.objects.all().order_by('-id')[:4],
        'conversion' : Conversion.objects.all().order_by('-id')[:3],
        

    }
    return render(request, 'index-1.html', context)

def service(request):
    context = {
        "info": Info.objects.last(),
        'logo' : logo.objects.last(),
        'view' : View.objects.last(),
        'project' : Project.objects.last(),
        'project_text' : Project_text.objects.last(),
        'about' : About.objects.last(),
        'suppor' : Suppor.objects.last(),
        'frequently' : Frequently.objects.last(),
        'frequently_text': Frequently_text.objects.last(),
        'communyte' : Communyte.objects.last(),
        'conversion' : Conversion.objects.all().order_by('-id')[:3],
    }
    return render(request, 'index-2.html', context)

def features(request):
    context = {
        "info": Info.objects.last(),
        'logo' : logo.objects.last(),
        'view' : View.objects.last(),
        'project' : Project.objects.last(),
        'project_text' : Project_text.objects.last(),
        'about' : About.objects.last(),
        'suppor' : Suppor.objects.last(),
        'frequently' : Frequently.objects.last(),
        'frequently_text': Frequently_text.objects.last(),
        'communyte' : Communyte.objects.last(),
        'conversion' : Conversion.objects.all().order_by('-id')[:3],
    }
    return render(request, 'index-3.html', context)

def user(request):
    context = {
        "info": Info.objects.last(),
        'logo' : logo.objects.last(),
        'view' : View.objects.last(),
        'project' : Project.objects.last(),
        'project_text' : Project_text.objects.last(),
        'about' : About.objects.last(),
        'suppor' : Suppor.objects.last(),
        'frequently' : Frequently.objects.last(),
        'frequently_text': Frequently_text.objects.last(),
        'communyte' : Communyte.objects.last(),
        'conversion' : Conversion.objects.all().order_by('-id')[:3],
    }
    return render(request, 'index-4.html', context)

def pricing(requset):
    context = {
        "info": Info.objects.last(),
        'logo' : logo.objects.last(),
        'project' : Project.objects.last(),
        'project_text' : Project_text.objects.last(),
        'about' : About.objects.last(),
        'suppor' : Suppor.objects.last(),
        'frequently' : Frequently.objects.last(),
        'frequently_text': Frequently_text.objects.last(),
        'communyte' : Communyte.objects.last(),
        'conversion' : Conversion.objects.all().order_by('-id')[:3],
    }
    return render(requset, 'index-5.html', context)

def faq(request):
    context = {
        "info": Info.objects.last(),
        'logo' : logo.objects.last(),
        'project' : Project.objects.last(),
        'project_text' : Project_text.objects.last(),
        'about' : About.objects.last(),
        'suppor' : Suppor.objects.last(),
        'frequently' : Frequently.objects.last(),
        'frequently_text': Frequently_text.objects.last(),
        'communyte' : Communyte.objects.last(),
        'conversion' : Conversion.objects.all().order_by('-id')[:3],
    }
    return render(request, 'index-6.html', context)

def blog(request):
    context = {
        "info": Info.objects.last(),
        'logo' : logo.objects.last(),  
        'project' : Project.objects.last(),
        'project_text' : Project_text.objects.last(),
        'about' : About.objects.last(),
        'suppor' : Suppor.objects.last(),
        'frequently' : Frequently.objects.last(),
        'frequently_text': Frequently_text.objects.last(),
        'communyte' : Communyte.objects.last(),
        'conversion' : Conversion.objects.all().order_by('-id')[:3],
    }
    return render(request, 'index-7.html', context)


