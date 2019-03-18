from django.shortcuts import render

# Create your views here.


from .models import TicTacToe

def index(request):
    """Show some summary stats about history of the naughts and crosses games, with a big ass new game button."""

def game(request, pk):
    """Play a game, will reload and update based on player moves.
    Request will include a form, which will either have a valid move to add, or nothing (indicating a game has only just started)."""
