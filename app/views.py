from django.shortcuts import render, redirect
from .forms import ingredient_formset, CaptchaField, todo_formset
from .models import Ingredients

def index(request):


    if request.method == 'POST':
        formset= todo_formset(request.POST)
        if formset.is_valid():
            formset.save()
        return redirect('index')
    else:
        formset=todo_formset()

    print(formset)
    return render(request, 'index.html', {'formset': formset})



def captcha(request):
    form = CaptchaField()

    return render(request, 'create.html', {'form':form})
