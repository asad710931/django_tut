from django import forms

class User(forms.Form):
    Name = forms.CharField()
    Email = forms.CharField()

