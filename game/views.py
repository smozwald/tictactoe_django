from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic.base import View
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import TicTacToe

class IndexView(View):
    """Show some summary stats about history of the naughts and crosses games, with a big ass new game button."""

    template = "game/index.html"

    def get(self, request):
        return render(request, self.template)

class GameView(View):
    """Play a game, will reload and update based on player moves.
    Request will include a form, which will either have a valid move to add, or nothing (indicating a game has only just started)."""
    template = "game/game.html"

    def get(self, request, pk):
        game = get_object_or_404(TicTacToe, pk = pk)
        board = game.board
        return render(request, self.template, {'id':pk, 'board':board})

def start_game(request):
    """Initialize a new game, and return it."""
    new_game = TicTacToe()
    new_game.save()
    new_id = new_game.id
    board = new_game.board
    return HttpResponseRedirect(reverse('game:game', args = (new_id)))

def make_move(request, pk):
    game = get_object_or_404(TicTacToe, pk=pk)
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            move = form.move
            game.make_move(move)

            return HttpResponseRedirect(reverse('game:game', args = (pk,)))



