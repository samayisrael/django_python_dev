from django import forms

class NameForm(forms.Form):
    things_pick = forms.CharField(label='Pickers', max_length=100, initial='Ryan, Blake, Josh, Conner')
    things_choice = forms.CharField(label='Choices', max_length=100, initial='Lizzy, Sarah, Zoey, Danica')


class DailyForm(forms.Form):
    foods = forms.CharField(label='Pickers', max_length=100, initial='Ryan, Blake, Josh, Conner')
    things_choice = forms.CharField(label='Choices', max_length=100, initial='Lizzy, Sarah, Zoey, Danica')
