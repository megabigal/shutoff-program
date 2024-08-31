from django import forms
from .models import checkboxModel

class loginForm(forms.Form):
    username = forms.CharField(label="usernametext", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
class usernameForm(forms.Form):
    username = forms.CharField(label="usernametext", max_length=100)
class toggleForm(forms.ModelForm):
    class Meta:
        model = checkboxModel
        fields = ['isChecked']