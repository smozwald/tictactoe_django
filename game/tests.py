from django.test import TestCase

# Create your tests here.
from .models import TicTacToe

class TicTacToeModelTests(TestCase):
    """Check that things work with the methods on TicTacToe."""

    def test_array_field_not_none(self):
        """The board isn't created, need to figure out why."""
        t = TicTacToe()
        self.assertTrue(t.board)
    
    def test_move_with_p1_updates_board_and_switches_to_p2(self):
        t = TicTacToe()
        t.make_move(0)
        self.assertEqual(t.board, [1,0,0,0,0,0,0,0,0])
        self.assertEqual(t.player, 2)

    def test_move_with_p2_updates_board_and_switches_to_p1(self):
        t = TicTacToe()
        t.make_move(0)
        t.make_move(4)
        self.assertEqual(t.board, [1,0,0,0,2,0,0,0,0])
        self.assertEqual(t.player, 1)

    def test_win_condition_p1_registers(self):
        t = TicTacToe()
        t.make_move(0)
        t.make_move(4)
        t.make_move(3)
        t.make_move(5)
        t.make_move(6)
        self.assertEqual(t.winner, "1")
        self.assertEqual(t.board,  [1,0,0,1,2,2,1,0,0])

    def test_win_condition_p2_registeres(self):
        t = TicTacToe()
        t.make_move(0)
        t.make_move(4)
        t.make_move(2)
        t.make_move(5)
        t.make_move(7)
        t.make_move(3)
        self.assertEqual(t.winner, "2")
        self.assertEqual(t.board,  [1,0,1,2,2,2,0,1,0])

    def test_draw_condition_registers(self):
        t = TicTacToe()
        t.make_move(1)
        t.make_move(0)
        t.make_move(3)
        t.make_move(2)
        t.make_move(4)
        t.make_move(5)
        t.make_move(6)
        t.make_move(7)
        t.make_move(8)
        self.assertEqual(t.winner, "D")
        self.assertEqual(t.board,  [2,1,2,1,1,2,1,2,1])

    def test_cant_play_with_winner_declared(self):
        t = TicTacToe()
        t.winner = "1"
        t.make_move(1)
        self.assertEqual(t.board,  [0,0,0,0,0,0,0,0,0])