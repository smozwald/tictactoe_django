from .models import TicTacToe
from django import forms

class InputForm(forms.Form):
    move = forms.IntegerField()