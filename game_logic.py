class GameLogic(object):
    print("Game Logic Object Created")
    # TODO add code here to manage the logic of your game
    def __init__(self, board, piece):
        liberties = []
        self.board = board
        self.stone = [piece]

        def remove(self):

            while self.stone:
                self.stone[0].remove()

            self.board.stone.remove()

        def rules(self):
            #if a move would enforce 0 liberties on a piece, it is invalid
            if 0 in liberties:
                self.remove()

