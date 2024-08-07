from django import forms
from .models import checkboxModel

class usernameForm(forms.Form):
    username = forms.CharField(label="usernametext", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
class toggleForm(forms.ModelForm):
    class Meta:
        model = checkboxModel
        fields = ['isChecked']