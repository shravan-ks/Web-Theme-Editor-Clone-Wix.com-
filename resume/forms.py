from django import forms

from resume.models import resumeDb


class createTH(forms.ModelForm):
    class Meta:
        model = resumeDb
        fields = ['Project_Name', 'Profile_Name', 'Address', 'Phone_Number','Email',]

class updatetDb(forms.ModelForm):
    About_Me = forms.CharField(widget=forms.Textarea)
    Skills = forms.CharField(widget=forms.Textarea)
    Experience = forms.CharField(widget=forms.Textarea )
    class Meta:
        model = resumeDb
        fields = ['Profile_Name', 'Profile_Picture', 'About_Me', 'Skills', 'Experience', 'Upload_Resumne','Address', 'Phone_Number','Email'
                  ]


class toolsDb(forms.ModelForm):
    class Meta:
        model = resumeDb
        fields = [
            'Facebook',
            'Instagram',
            'Twitter',
            'GitHub',
            'Background_Color_Left_Column',
            'Background_Color_Right_Column',
            'Accent_Color',
        ]