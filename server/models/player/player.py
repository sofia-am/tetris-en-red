import string, random
from ..board.board import Board

class Player:

    @classmethod
    def generate_id(cls):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(6))

    IDDLE = 'IDDLE'
    PENDING = 'PENDING'
    READY = 'READY'
    PLAYING = 'PLAYING'
    SPECTATING = 'SPECTATING'

    def __init__(self, name, avatar):
        self.id = Player.generate_id()
        self.name = name
        self.avatar = avatar
        self.state = Player.IDDLE
        self.score = 0
        self.count = 0
        self.lines = 0
        self.tetris = 0
        self.board = Board(20, 10)

    def action_move_left(self):
        self.board.active_piece.x -= 1
        self.apply_action({"x": 1})
    
    def action_move_right(self):
        self.board.active_piece.x += 1
        self.apply_action({"x": -1})
    
    def action_rotate_clock(self):
        self.board.active_piece.x += 1
        self.apply_action({"rotation": -1})
    
    def action_rotate_unclock(self):
        self.board.active_piece.x -= 1
        self.apply_action({"rotation": +1})
    
    def action_accelerate(self):
        self.board.active_piece.x += 1
        self.apply_action({"y": 1})

    def apply_action(self, correction):
        self.board.active_piece.calculate_blocks()
        if not self.board.active_piece.check_state(self.board.positions):
            if "x" in correction:
                self.board.active_piece.x += correction["x"]
            if "y" in correction:
                self.board.active_piece.x += correction["y"]
            if "rotation" in correction:
                self.board.active_piece.x += correction["rotation"]

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "avatar": self.avatar,
            "state": self.state,
            "score": self.score,
            "count": self.count,
            "lines": self.lines,
            "tetris": self.tetris,
        }