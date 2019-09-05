from django import forms

from feeback.models import feedbackform


class feedform(forms.ModelForm):
    Your_Message = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = feedbackform
        fields = ['Subject','Your_Message',]