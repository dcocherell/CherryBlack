from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms.input_form import FinancialDataForm

@login_required
def home(request):
    return render(request, 'home.html', {'message': 'Welcome to CherryBlack!'})

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def input_financial_data(request):
    if request.method == "POST":
        form = FinancialDataForm(request.POST)  # use the form class
        if form.is_valid():
            # save the data or do something with it
            return redirect('home')  # or redirect somewhere else
    else:
        form = FinancialDataForm()  # use the form class
    return render(request, 'input_financial_data.html', {'form': form})
