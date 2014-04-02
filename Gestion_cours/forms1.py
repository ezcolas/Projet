from django import forms 

class loginForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.PasswordField(max_length=10)
     
