from django.shortcuts import render, redirect

# Create your views here.
from theme1.forms import CreateTh1, Th1_console
from theme1.models import theme1


def theme1_view(request):
    return render(request, 'theme1/index.html')


def create_theme1(request):
    form = CreateTh1(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('view_theme1')

    return render(request, 'theme1/create.html', {'form': form})


def view_theme1(request, id):
    theme_view = theme1.objects.filter(id=id)
    return render(request, 'theme1/view.html', {'theme_view': theme_view})
#
# def theme1_console(request, id):
#     theme_con = theme1.objects.get(id=id)
#     theme_view = theme1.objects.filter(id=id)
#     form = Th1_console(request.POST, instance=theme_con)
#
#     if form.is_valid():
#         form.save()
#     return render(request, 'theme1/console.html', {'form': form, 'theme_con': theme_con, 'theme_view': theme_view })


def theme1_console(request, id):
    theme_con = theme1.objects.get(id=id)
    theme_view = theme1.objects.filter(id=id)
    form = Th1_console(request.POST or None, request.FILES or None, instance=theme_con)
    if form.is_valid():
        form.save()
        return redirect('list_theme')

    return render(request, 'theme1/console.html', {'form': form, 'theme_con': theme_con, 'theme_view':theme_view })

def list_theme(request):
    list_Th = theme1.objects.all()
    return render(request, 'home.html', {'list_Th': list_Th})


# def theme1_console(request, id):
#     theme_con = theme1.objects.get(id=id)
#     theme_view = theme1.objects.filter(id=id)
#     if request.method == 'POST':
#         form = Th1_console(request.POST or None, prefix='banned', instance=theme_con)
#         if form.is_valid():
#             form.save()
#     else:
#         form = Th1_console(prefix='banned')
#
#     if request.method == 'POST' and not form.is_valid():
#         forms = Th1_console2(request.FILES or None, prefix='expected', instance=theme_con)
#         form = Th1_console(prefix='banned')
#         if forms.is_valid():
#             forms.save()
#     else:
#         forms = Th1_console2(prefix='expected')
#
#     return render(request, 'theme1/console.html', {'form': form, 'theme_con': theme_con, 'theme_view': theme_view,'forms': forms  })