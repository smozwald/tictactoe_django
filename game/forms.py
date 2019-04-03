from .models import TicTacToe
from django import forms

class InputForm(forms.form):
    game_id = IntegerField()
    move = IntegerField()