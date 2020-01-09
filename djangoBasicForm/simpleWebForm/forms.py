from django import forms
class FormName(forms.Form):
    """docstring for ."""
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget =forms.Textarea)
