from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from Company.forms import createCom, updateCom, toolsCom
from Company.models import CompanyDb
from resume.forms import toolsDb


def index(request):
    return render(request, 'Company/index.html')

def create(request):
    form = createCom(request.POST or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('company:index',)
    return render(request,'Company/create.html', {'form':form})


def console(request, Project_Name):
    theme_con = CompanyDb.objects.get(Project_Name=Project_Name)
    theme_view = CompanyDb.objects.filter(Project_Name=Project_Name)
    form = updateCom(request.POST or None, request.FILES or None, instance=theme_con)
    if form.is_valid():
        form.save()
    return render(request, 'Company/console.html', {'form': form, 'theme_con': theme_con, 'theme_view':theme_view})


def view(request, Project_Name):
    theme_view = CompanyDb.objects.filter(Project_Name=Project_Name)
    return render(request, 'Company/view.html', {'theme_view': theme_view})


def delete(request, Project_Name):
    theme_delete = CompanyDb.objects.get(Project_Name=Project_Name)
    if request.method == 'POST':
        theme_delete.delete()
        return redirect('core:dashboard')

    return render(request, 'Company/delete.html', {'theme_delete': theme_delete})


def tools(request, Project_Name,):
    theme_con = CompanyDb.objects.get(Project_Name=Project_Name)
    theme_view = CompanyDb.objects.filter(Project_Name=Project_Name)
    ph_num =  CompanyDb.objects.filter(Project_Name=Project_Name).values_list('Phone_Number', flat=True).first()
    brandname = CompanyDb.objects.filter(Project_Name=Project_Name).values_list('Brand_Name', flat=True).first()
    emails = CompanyDb.objects.filter(Project_Name=Project_Name).values_list('Email', flat=True).first()
    contacts = {
        'name': brandname,
        'phone_number': ph_num,
        'email': emails,
        'url': request.build_absolute_uri(reverse('company:view' , args=(Project_Name, ))),
        'company': brandname,
    }
    form = toolsCom(request.POST or None, request.FILES or None, instance=theme_con)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'Company/tools.html',{'form': form, 'theme_con': theme_con, 'theme_view': theme_view,'contacts':contacts})