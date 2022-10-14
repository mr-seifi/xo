from game.models import Player, Game


class GameService:

    def __init__(self, game: Game) -> None:
        self.game = game
        self.turn: Player = game.player_1
    
    def change_turn(self) -> None:
        if self.turn == self.game.player_1:
            self.turn: Player = self.game.player_2
        else:
            self.turn: Player = self.game.player_1

    def is_turn(self, id: int) -> bool:
        return self.turn.id == id
    
    def check_winning(self) -> int:
        if x := self.game.board.all_x_moves() and not sum(x) % 3:
            return 1
        elif o := self.game.board.all_o_moves() and not sum(o) % 3:
            return 2
        return -1