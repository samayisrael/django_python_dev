from django import forms

class NameForm(forms.Form):
    stable_detail = forms.CharField(label='Your name', max_length=100)
