from django import forms

class SignUpForm(forms.Form):
    FirstName = forms.CharField(label="First Name", max_length=100)
    LastName = forms.CharField(label="Last Name", max_length=100)
    UserName = forms.CharField(label="User Name", max_length=100)
    Password = forms.CharField(label="Password", widget=forms.PasswordInput())
    Email = forms.EmailField(label="Email", required=True)

class LoginForm(forms.Form):
    UserName = forms.CharField(label="User Name", max_length=100)
    Password = forms.CharField(label="Password", widget=forms.PasswordInput())