from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('expense/new/', views.add_expense, name='add_expense'),
    path('expense/<int:expense_id>/', views.view_expense, name='view_expense'),
]