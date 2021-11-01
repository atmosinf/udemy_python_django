from django.shortcuts import render
from . import forms


# Create your views here.

def form(request):
    form = forms.MyNewForm()

    if request.method == 'POST':
        form = forms.MyNewForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
        else:
            print('ERROR. FORM INVALID')


    return render(request,'formsapp/form_page.html',{'form':form})
