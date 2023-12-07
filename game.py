# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 17:15:50 2022

@author: ritwick
"""
import numpy as np
import random
import keyboard
from IPython import get_ipython

class Board:
    def __init__(self,size):
        self.size = size
        self.score = 0
        self.board = np.zeros((size,size),dtype='int')
        r1 = random.randint(0, size-1)
        c1 = random.randint(0, size-1)
        r2 = random.randint(0, size-1)
        c2 = random.randint(0, size-1)
        if (r1 == r2 and c1 == c2):
            r2 = r2+1%size
        self.board[r1,c1] = 2
        self.board[r2,c2] = 2
        self.board_history = [self.board]
        
    def shift(self):
        temp = np.zeros((self.size,self.size),dtype='int')
        for i in range(self.size):
            fill_pos = 0
            for j in range(self.size):
                if self.board[i,j] != 0:
                    temp[i,fill_pos] = self.board[i,j]
                    fill_pos += 1
        self.board = temp
        
    def combine(self):
        for i in range(self.size):
            for j in range(self.size-1):
                if self.board[i,j] != 0 and self.board[i,j] == self.board[i,j+1]:
                    self.board[i,j] += self.board[i,j]
                    self.board[i,j+1] = 0
                    self.score += self.board[i,j]
                    
    def flip(self):
        temp = np.zeros((self.size,self.size), dtype='int')
        for i in range(self.size):
            for j in range(self.size):
                temp[i,j] = self.board[i,self.size-1-j]
        self.board = temp
        
    def transpose(self):
        self.board = self.board.T                    
        
    def add_number(self):
        if ((self.board==0).any() and not np.array_equal(self.board_history[-1], self.board)):
            row = random.randint(0, self.size-1)
            num = self.generate()
            flag = True
            while flag:
                for j in range(self.size):
                    if self.board[row,j] == 0:
                        self.board[row,j] = num
                        flag = False
                        break
                row = random.randint(0, self.size-1)
        else:
            pass
        
    def generate(self):
        n = random.random()
        if n<0.33:
            return 4
        return 2
        
    def show(self):
        print('Score : ',self.score)
        print(self.board)
        
    def left(self):
        self.shift()
        self.combine()
        self.shift()
        self.add_number()
        self.update_history()
        return self.game_over()

    def right(self):
        self.flip()
        self.shift()
        self.combine()
        self.shift()
        self.flip()
        self.add_number()
        self.update_history()
        return self.game_over()

    def up(self):
        self.transpose()
        self.shift()
        self.combine()
        self.shift()
        self.transpose()
        self.add_number()
        self.update_history()
        return self.game_over()

    def down(self):
        self.transpose()
        self.flip()
        self.shift()
        self.combine()
        self.shift()
        self.flip()
        self.transpose()
        self.add_number()
        self.update_history()
        return self.game_over()
        
    def game_over(self):
        if not (self.board==0).any() and not self.check():
            return True
            
        return False
    
    def check(self):
        for i in range(self.size):
            for j in range(self.size-1):
                if self.board[i,j] == self.board[i,j+1]:
                    return True
        
        for i in range(self.size-1):
            for j in range(self.size):
                if self.board[i,j] == self.board[i+1,j]:
                    return True
        
        return False
    
    def update_history(self):
        self.board_history.append(self.board)
    
    def print_history(self):
        for board in self.board_history:
            print(board)
            print()

        
def main():
    num = int(input('size : '))
    b = Board(num)
    game_over = False
    while not game_over:
        b.show()
        key = input('key : ')
        if key == 'w':
            game_over = b.up()
        elif key == 's':
            game_over = b.down()
        elif key == 'a':
            game_over = b.left()
        elif key == 'd':
            game_over = b.right()
        else:
            continue
        
    b.show()
    print('game over')

    print('history')
    b.print_history()
        
if __name__ == '__main__':
    main()
        
    
    