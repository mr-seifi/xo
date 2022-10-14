from typing import List
from django.db import models


class Player(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    uname = models.CharField(max_length=255)


class Board(models.Model):
    X = 'X'
    O = 'O'

    BOARD_CHOICES = [
        (X, 'X'),
        (O, 'O')
    ]
    x1 = models.CharField(choices=BOARD_CHOICES, null=True, max_length=2)
    x2 = models.CharField(choices=BOARD_CHOICES, null=True, max_length=2)
    x3 = models.CharField(choices=BOARD_CHOICES, null=True, max_length=2)
    y1 = models.CharField(choices=BOARD_CHOICES, null=True, max_length=2)
    y2 = models.CharField(choices=BOARD_CHOICES, null=True, max_length=2)
    y3 = models.CharField(choices=BOARD_CHOICES, null=True, max_length=2)
    z1 = models.CharField(choices=BOARD_CHOICES, null=True, max_length=2)
    z2 = models.CharField(choices=BOARD_CHOICES, null=True, max_length=2)
    z3 = models.CharField(choices=BOARD_CHOICES, null=True, max_length=2)
    
    @staticmethod
    def _pos_to_char(pos: int) -> str:
        return f'{chr(120 + pos // 3)}{pos % 3 + 1}'

    def is_accessible(self, pos: int) -> bool:
        return getattr(self, self._pos_to_char(pos)) == None
    
    def all_x_moves(self) -> List[int]:
        _e = self.__dict__.copy()
        _e.pop('_state')
        _e.pop('id')

        return [it for it, ch in enumerate(_e) if _e[ch] == self.X]
    
    def all_o_moves(self) -> List[int]:
        _e = self.__dict__.copy()
        _e.pop('_state')
        _e.pop('id')

        return [it for it, ch in enumerate(_e) if _e[ch] == self.O]

    def __repr__(self) -> str:
        return f'{self.x1}|{self.x2}|{self.x3}\n' \
               f'{self.y1}|{self.y2}|{self.y3}\n' \
               f'{self.z1}|{self.z2}|{self.z3}'

class Game(models.Model):
    player_1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='+')
    player_2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='+')
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __repr__(self) -> str:
        return self.board
