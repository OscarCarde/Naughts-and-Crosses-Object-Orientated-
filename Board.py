from typing import List

from Player import Player


MAX_HEIGHT = 3
MAX_WIDTH = 3

class Board():
    def __init__(self):
        """
        Initialises a matrix  that stores the moves
        """
        self.cells = [[' ' for item in range(MAX_HEIGHT)] for other in range(MAX_WIDTH)]

    # @classmethod
    # def getSize():
    #     return len(self.cells)

    def display(self):
        """
        Terminal representation of the board
        """
        print(" ",self.cells[0][0]," | ",self.cells[1][0]," | ",self.cells[2][0]," ") #automate this like (embedded list comprehension)
        print("_________________")
        print(" ",self.cells[0][1]," | ",self.cells[1][1]," | ",self.cells[2][1]," ")
        print("_________________")
        print(" ",self.cells[0][2]," | ",self.cells[1][2]," | ",self.cells[2][2]," ")
        
    def updatecell(self, moveCoordinate: List, player: Player):
        """
        Updates the representative matrix when the player moves
        """
        
        x = moveCoordinate[0]
        y = moveCoordinate[1]

        if self.cells[x][y] == ' ':
            self.cells[x][y] = player.name
    
    def resetBoard(self, board: List[List]):
        """
        Resets the board when a user wants to play again
        """
        for item in board:
            item = ' '