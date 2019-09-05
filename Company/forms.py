from django import forms

from Company.models import CompanyDb


class createCom(forms.ModelForm):
    class Meta:
        model = CompanyDb
        fields = ['Project_Name', 'Brand_Name', 'Address', 'Phone_Number','Email',]


class updateCom(forms.ModelForm):
    Banner_Text = forms.CharField(widget=forms.Textarea)
    Our_Services = forms.CharField(widget=forms.Textarea)
    About_Us = forms.CharField(widget=forms.Textarea )
    class Meta:
        model = CompanyDb
        fields = ['Brand_Name', 'Brand_Logo', 'Banner_Heading', 'Banner_Text', 'Our_Services', 'About_Us','Address', 'Phone_Number','Email'
                  ]


class toolsCom(forms.ModelForm):
    class Meta:
        model = CompanyDb
        fields = [
            'Facebook',
            'Instagram',
            'Twitter',
            'Background_Color_Banner',
            'Background_Color_Service',
            'Background_Color_About',
            'Background_Color_Navbar',
            'Accent_Color',
        ]