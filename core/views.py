from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
from Company.models import CompanyDb
from core.forms import updateprofile
from core.models import notification
from restaurant.models import RestDb
from resume.models import resumeDb
from theme1.models import theme1


def indexweb(request):
    return render(request, 'core/index.html')


def dashboard(request):
    if request.user.is_authenticated:
        th1 = theme1.objects.all()
        th2 = RestDb.objects.all()
        th3 = resumeDb.objects.all()
        th4 = CompanyDb.objects.all()
        return render(request, 'core/dashboard.html', {'th1': th1, 'th2':th2, 'th3':th3, 'th4':th4})
    else:
        return redirect('account_login')


def search_themes(request):
    if request.user.is_authenticated:
        return render(request, 'core/search_themes.html',)
    else:
        return redirect('account_login')

#
# def search_themes(request):
#     if request.user.is_authenticated:
#         listTh1 = theme1.objects.all()
#         cruds = crud.objects.all()
#         return render(request, 'core/search_themes.html', {'listTh1': listTh1, 'cruds': cruds})
#     else:
#         return redirect('account_login')
def notify (request):
    notify = notification.objects.all()
    return render(request, 'core/notification.html',{'notify':notify})


def updateuser(request, username):
    pro = User.objects.get(username=username)
    pros = User.objects.filter(username=username)
    form = updateprofile(request.POST or None, instance=pro)
    if form.is_valid():
        form.save()
        return redirect('core:dashboard')

    return render(request, 'core/profile.html', {'form': form, 'pro': pro,'pros':pros })