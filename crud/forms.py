from django import forms

from crud.models import crud


class CrudHome(forms.ModelForm):
    class Meta:
        model = crud
        fields = ['description', 'name',]



class CrudUpdate(forms.ModelForm):
    class Meta:
        model = crud
        fields = ['description', 'name', 'section',]
