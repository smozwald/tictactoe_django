from .models import TicTacToe
from django import forms

class InputForm(forms.form):
    move = IntegerField()