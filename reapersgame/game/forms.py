from django import forms

class userform(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password')

class registerform(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    email = forms.CharField(label='E-mail')