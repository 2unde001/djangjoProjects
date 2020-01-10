from django.shortcuts import render
from . import forms

# Create your views here.
def HomePageView(request):
    return render(request, 'formsApp/form_home.html')

def ContactFormPageView(request):
    form = forms.UserForm()

    if request.method == 'POST':
        form = forms.UserForm(request.POST)

        if form.is_valid():
            print('FORM VALIDATION')
            print('Title: '+form.cleaned_data['title'])
            print('Name: '+form.cleaned_data['name'])
            print('Email: '+form.cleaned_data['email'])
            print('Text: '+form.cleaned_data['text'])

    return render(request, 'formsApp/contact_form.html', {'form':form})
