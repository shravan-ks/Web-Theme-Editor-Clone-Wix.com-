from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from resume.forms import createTH, updatetDb, toolsDb
from resume.models import resumeDb


def index(request):
    return render(request, 'resume/index.html')

# def create(request):
#     form = resumeDb(request.POST or None)
#     if form.is_valid():
#         form = form.save(commit=False)
#         form.user = request.user
#         form.save()
#         return redirect('restaurant:console', form.projectname  )
#
#     return render(request, 'restaurant/create.html', {'form': form})

def create(request):
    form = createTH(request.POST or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('resume:console', form.Project_Name )
    return render(request,'resume/create.html', {'form':form})


def console(request, Project_Name):
    theme_con = resumeDb.objects.get(Project_Name=Project_Name)
    theme_view = resumeDb.objects.filter(Project_Name=Project_Name)
    form = updatetDb(request.POST or None, request.FILES or None, instance=theme_con)
    if form.is_valid():
        form.save()
    return render(request, 'resume/console.html', {'form': form, 'theme_con': theme_con, 'theme_view':theme_view})

def view(request, Project_Name):
    theme_view = resumeDb.objects.filter(Project_Name=Project_Name)
    return render(request, 'resume/view.html', {'theme_view': theme_view})


def delete(request, Project_Name):
    theme_delete = resumeDb.objects.get(Project_Name=Project_Name)
    if request.method == 'POST':
        theme_delete.delete()
        return redirect('core:dashboard')

    return render(request, 'resume/delete.html', {'theme_delete': theme_delete})

def tools(request, Project_Name,):
    theme_con = resumeDb.objects.get(Project_Name=Project_Name)
    theme_view = resumeDb.objects.filter(Project_Name=Project_Name)
    ph_num =  resumeDb.objects.filter(Project_Name=Project_Name).values_list('Phone_Number', flat=True).first()
    brandname = resumeDb.objects.filter(Project_Name=Project_Name).values_list('Profile_Name', flat=True).first()
    emails = resumeDb.objects.filter(Project_Name=Project_Name).values_list('Email', flat=True).first()
    contacts = {
        'name': brandname,
        'phone_number': ph_num,
        'email': emails,
        'url': request.build_absolute_uri(reverse('resume:view' , args=(Project_Name, ))),
        'company': brandname,
    }
    form = toolsDb(request.POST or None, request.FILES or None, instance=theme_con)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'resume/tools.html',{'form': form, 'theme_con': theme_con, 'theme_view': theme_view,'contacts':contacts})
