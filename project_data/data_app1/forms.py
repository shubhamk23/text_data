# forms.py

from django import forms

class UploadFileForm(forms.Form):
    # file = forms.FileField(widget=forms.ClearableFileInput(attrs={ 'multiple': True} ))
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={ 'allow_multiple_selected': True}), required=False)

    
