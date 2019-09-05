from django import forms

from restaurant.models import RestDb


class createRestDb(forms.ModelForm):
    class Meta:
        model = RestDb
        fields = ['projectname', 'brandname', ]


class updateRestDb(forms.ModelForm):
    about = forms.CharField(widget=forms.Textarea)
    brandname = forms.CharField(max_length=50, label='Brand Name')
    class Meta:
        model = RestDb
        fields = ['brandname', 'brandimg', 'about', 'ph_num', 'review_link', 'menu',
                  'gallery1','gallery2','gallery3','gallery4','gallery5','gallery6','gallery7','gallery8',
                  'address','maps',
                  ]


class toolsgs(forms.ModelForm):
    class Meta:
        model = RestDb
        fields = [
            'favicon',
            'Facebook',
            'Instagram',
            'Twitter',
            'title',
            'description',
            'Social_Title',
            'Social_Image',
            'Social_Description',
        ]

# class toolseo(forms.ModelForm):
#     class Meta:
#         model = RestDb
#         fields = [
#             'title',
#             'description',
#             'Social_Title',
#             'Social_Image',
#             'Social_Description',
#         ]

# class toolcontact(forms.ModelForm):
#     class Meta:
#         model = RestDb
#         fields = [
#             'title',
#             'description',
#             'Social_Title',
#             'Social_Image',
#             'Social_Description',
#         ]

# class Contact(forms.ModelForm):
#     class Meta:
#         model = RestDb
#         fields = [
#             'Name',
#             'Email',
#             'Your_Message',
#         ]