from django import forms

from theme1.models import theme1


class CreateTh1(forms.ModelForm):
    class Meta:
        model = theme1
        fields = ['projectname', 'brand_name',]


class Th1_console(forms.ModelForm):
    brand_name = forms.CharField(label='Company Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    menu1 = forms.CharField(label='First Menu', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    menu2 = forms.CharField(label='Second Menu', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    menu3 = forms.CharField(label='Third Menu', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    menu4 = forms.CharField(label='Fourth Menu', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    brandimg = forms.ImageField(label='Company Logo', required=False,)
    class Meta:
        model = theme1
        fields = ['brand_name', 'menu1', 'menu2','menu3','menu4','brandimg', ]



# class Th1_console2(forms.ModelForm):
#     brandimg = forms.ImageField(label='Company Logo', required=False)
#     class Meta:
#         model = theme1
#         fields = ['brandimg',]
