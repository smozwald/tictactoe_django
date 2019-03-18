from django.db import models
from django.contrib.postgres.fields import ArrayField
import numpy as np

# Create your models here.

def default_board(size = 3):
    """Will return an x*x board. Could be used to improve later to have default options, if desired."""
    return list([0] * (size*size))

class TicTacToe(models.Model):
    """From previously made python class TicTacToe, adapted to work as a Django class.
    Also based on the github page https://github.com/claudiordgz/tictactoe-django/blob/master/game/models.py
    which has been inspirational in building this app."""

    board = ArrayField(models.IntegerField(), default = default_board, size = 9,)
    total_moves = models.IntegerField(default = 0)
    player = models.IntegerField(default = 1)
    winner = models.CharField(max_length = 1, default = "N") #Can be N when in progress, D if drawn, or 1/2 for p1/2

    def make_move(self, move):
        """Make a move for each player, check its valid and victory condition.
        Moves can be 0 - 8 when input from web.
        """
        player = self.player
        if self.winner != "N":
            return
        try:
            self.update_board(player, move)
            self.total_moves += 1
            
            self.check_victory()
            if self.player == 1:
                self.player = 2
            else:
                self.player = 1
        except:
            ##Shouldn't be possible for user to fail, this is for testing purposes
            return "Failed"

    def update_board(self, player, move):

        ##TO DO: Update player aswell.
        """Updates the board when a valid move is made."""
        num = player
        if (self.board[move] == 0):
            self.board[move] = player
        else:
            Exception()
    
    def check_victory(self):

        ##TO DO: FIGURE OUT HOW TO WORK THIS NUMPY STUFF
        ##TO DO: CHANGE VICTORY TO AN ALTERATION OF THE MODEL FIELD.
        """Checks if victory condition of 3 in a row met."""
        check_board = np.zeros((3,3)) ##Update this to size if you change it
        for i in range(3):
            for j in range(3):
                check_board[i,j] = self.board[0+i*3 + j]
        for i in range(3):
            if ((np.all(check_board[i,:] == check_board[i,0])) 
                and (check_board[i,0] != 0)):
                    self.winner = str(self.player)
            if ((np.all(check_board[:, i] == check_board[0,i])) 
                and (check_board[0,i] != 0)):
                    self.winner = str(self.player)
        ##Also check diagonal
        if (((check_board[0,0] == check_board[1,1] == check_board[2,2])
            or (check_board[2,0] == check_board[1,1] == check_board[0,2]))
            and check_board[1,1] != 0):
            self.winner = str(self.player)
        else:
            if self.total_moves >= 9:
                self.winner = "D"