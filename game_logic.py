class GameLogic(object):
    print("Game Logic Object Created")
    # TODO add code here to manage the logic of your game
    def __init__(self, board, piece):
        liberties = []
        self.board = board
        self.stone = [piece]

    def makeMove(self, col, row):
            '''tries to move'''
            if self.isEmpty(col, row):  # check if the space is empty
                if self.notKO(col, row):  # checks to make sure it is not a KO
                    self.createListofPlayerLocationsAroundCurrentMoveAndLibertyCount(col,
                                                                                     row)  # call specified function, explained below
                    self.create4ListsOfOppoentLocationsAroundCurrentMoveLocationAnd4LibertyCounts(col,
                                                                                                  row)  # call specified function, explained below
                    self.capture()  # capture pieces
                    if self.notSuicide(col, row):  # check to see if it is a Suicide move
                        self.placePiece(col, row)  # place the peice
                        self.updateScoreBoard()  # update the score board
                        self.checkWinner()  # see if there is a winner
                        self.switchPlayer()  # switch the player
                        self.update()  # referesh the widget


        def remove(self):

            while self.stone:
                self.stone[0].remove()



        def withinBoardRange(self, col, row):
            ''' Check to see if the col and row are within the board number of columns and rows
                    returns true if they are
                    returns false if they are not'''
            if row in self.board.row:
                if col in self.board.col:
                    return True
                else:
                    return False

        def notInLocationList(self, list, col, row):
                '''returns true if the col and row is not in the list'''
                if col not in list:
                    if row not in list:
                        return True
                    else:
                        return False

        def isEmpty(self, col, row):
            '''Checks to see if the location specified by the row and col empty'''
            if 0 in col:
                if 0 in row:
                    return True
            else:
                return False
