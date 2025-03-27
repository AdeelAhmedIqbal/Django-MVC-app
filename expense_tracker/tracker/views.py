from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum

@login_required
def home(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-expense_date')
    total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    return render(request, 'home.html', {'expenses': expenses, 'total': total})

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('home')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

@login_required
def view_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    return render(request, 'view_expense.html', {'expense': expense})