from django.shortcuts import render, redirect

from crud.forms import CrudHome, CrudUpdate
from crud.models import crud


def list_crud(request):
    cruds = crud.objects.all()
    return render(request, 'index.html', {'cruds': cruds})


def create_crud(request):
    form = CrudHome(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_crud')

    return render(request, 'cruds.html', {'form': form})

def update_crud(request, id):
    cruds = crud.objects.get(id=id)
    form = CrudUpdate(request.POST or None, instance=cruds)

    if form.is_valid():
        form.save()
        return redirect('list_crud')

    return render(request, 'cruds.html', {'form': form, 'cruds': cruds })

def delete_crud(request, id):
    crud_del = crud.objects.get(id=id)
    if request.method == 'POST':
        crud_del.delete()
        return redirect('list_crud')

    return render(request, 'delete.html', {'crud_del': crud_del})
