from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from restaurant.forms import createRestDb, updateRestDb, toolsgs
from restaurant.models import RestDb, RestDbContact


def index(request):
    return render(request, 'restaurant/index.html')

# def create(request):
#     return render(request, 'restaurant/create.html')

def create(request):
    form = createRestDb(request.POST or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('restaurant:console', form.projectname  )

    return render(request, 'restaurant/create.html', {'form': form})

def console(request, projectname):
    theme_con = RestDb.objects.get(projectname=projectname)
    theme_view = RestDb.objects.filter(projectname=projectname)
    form = updateRestDb(request.POST or None, request.FILES or None, instance=theme_con)
    if form.is_valid():
        form.save()


    return render(request, 'restaurant/console.html', {'form': form, 'theme_con': theme_con, 'theme_view':theme_view})


def view(request, projectname):
    theme_view = RestDb.objects.filter(projectname=projectname)
    if  request.method == 'POST':
        username = request.POST.get("username")
        useremail = request.POST.get("useremail")
        message = request.POST.get("message")
        theme = request.POST.get("theme")
        contact = RestDbContact()
        contact.Name = username
        contact.Email = useremail
        contact.Your_Message = message
        contact.theme_id = theme
        contact.save()
    return render(request, 'restaurant/view.html', {'theme_view': theme_view})

def delete(request, projectname):
    theme_delete = RestDb.objects.get(projectname=projectname)
    if request.method == 'POST':
        theme_delete.delete()
        return redirect('core:dashboard')

    return render(request, 'restaurant/delete.html', {'theme_delete': theme_delete})

# def theme1_console(request, id):
#     theme_con = theme1.objects.get(id=id)
#     theme_view = theme1.objects.filter(id=id)
#     form = Th1_console(request.POST or None, request.FILES or None, instance=theme_con)
#     if form.is_valid():
#         form.save()
#         return redirect('list_theme')
#
#     return render(request, 'theme1/console.html', {'form': form, 'theme_con': theme_con, 'theme_view':theme_view })
#
def tools(request, projectname,):
    contact = RestDbContact.objects.all()
    theme_con = RestDb.objects.get(projectname=projectname)
    theme_view = RestDb.objects.filter(projectname=projectname)
    ph_num =  RestDb.objects.filter(projectname=projectname).values_list('ph_num', flat=True).first()
    brandname = RestDb.objects.filter(projectname=projectname).values_list('brandname', flat=True).first()
    contacts = {
        'name': brandname,
        'phone_number': ph_num,
        'email': 'foo@example.com',
        'url': request.build_absolute_uri(reverse('restaurant:view' , args=(projectname, ))),
        'company': brandname,
    }
    form = toolsgs(request.POST or None, request.FILES or None, instance=theme_con)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'restaurant/tools.html',{'form': form, 'theme_con': theme_con, 'theme_view': theme_view, 'contact':contact,'contacts':contacts})

