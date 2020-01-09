from django.shortcuts import render
from . import forms
# Create your views here.
def home(request):
     return render(request, "home.html")

def form_name_views(request):
    form = forms.FormName()

    if request == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():

            print("VALIDATION SUCCESS")
            print("NAME: "+form.clean_data['name'])
            print("EMAIL: "+form.clean_data['email'])
            print("TEXT: "+form.clean_data['text'])
            
    return render(request, 'form_page.html', {'form':form})
