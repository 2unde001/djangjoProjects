from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("NAME NEED TO START WITH Z")

class UserForm(forms.Form):
    """
    Using Django build in validator
    to prevent unwanted srapping/BOT
    on our website
    """
    title = forms.CharField()
    # name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    very_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
    widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    """
    Validate user email
    If user email do not match, clean the form, and display
    validation error
    
    """
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['very_email']

        if email != vemail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH")
