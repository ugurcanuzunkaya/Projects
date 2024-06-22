from django import forms


class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    available_date = forms.DateField()
    occupation = forms.CharField(max_length=50)