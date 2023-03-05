from django import forms

class CompleteSignupForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    first_name = forms.CharField(label='First Name', max_length=30, required=True)
    last_name = forms.CharField(label='Last Name', max_length=30, required=True)
    mobile = forms.CharField(label='Mobile', max_length=30, required=True)
    age = forms.IntegerField(label='Age', required=True)
    address = forms.CharField(label='Address', widget=forms.Textarea(attrs={"rows":5, "cols":20}))
