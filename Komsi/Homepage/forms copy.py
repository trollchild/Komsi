from django import forms

class ContactForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100, required=False)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField(required=False)
    cc_myself = forms.BooleanField(required=False)
    phone = forms.CharField(max_length=100)
