from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'description', 'amount', 'expense_date']
        widgets = {
            'expense_date': forms.DateInput(attrs={'type':'date'})
        }