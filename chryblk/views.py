from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms.input_form import FinancialDataForm
from .models import FinancialData

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
    if request.method == 'POST':
        form = FinancialDataForm(request.POST)
        if form.is_valid():
            # Instead of form.save(), we manually create a FinancialData object.
            financial_data = FinancialData()
            financial_data.date = form.cleaned_data.get('date')
            financial_data.income = form.cleaned_data.get('income')
            financial_data.expense = form.cleaned_data.get('expense')
            financial_data.expense_type = form.cleaned_data.get('expense_type')
            financial_data.state = form.cleaned_data.get('state')
            financial_data.user = request.user
            financial_data.save()

            return redirect('chryblk:home')
    else:
        form = FinancialDataForm()

    return render(request, 'input_financial_data.html', {'form': form})

@login_required
def report(request):
    # Get all the financial data for the current user.
    financial_data = FinancialData.objects.filter(user=request.user)

    # Calculate the total income and total expense.
    total_income = 0
    total_expense = 0
    for data in financial_data:
        total_income += data.income
        total_expense += data.expense

    # Calculate the net income.
    net_income = total_income - total_expense

    # Calculate the average income and average expense.
    average_income = total_income / len(financial_data)
    average_expense = total_expense / len(financial_data)

    # Calculate the average net income.
    average_net_income = average_income - average_expense

    return render(request, 'report.html', {
        'financial_data': financial_data,
        'total_income': total_income,
        'total_expense': total_expense,
        'net_income': net_income,
        'average_income': average_income,
        'average_expense': average_expense,
        'average_net_income': average_net_income,
    })
