#%%

import numpy as np
import random
import keyboard
import game
import time
import matplotlib.pyplot as plt
from collections import Counter

def game_run(b):
    game_over = False
    while not game_over:
        # print(b.score)
        # 0: up 1: down 2: left 3: right
        key = np.random.randint(4)
        if key == 0:
            game_over = b.up()
        elif key == 1:
            game_over = b.down()
        elif key == 2:
            game_over = b.left()
        elif key == 3:
            game_over = b.right()
        else:
            continue
    
    # b.print_history()

    return b.score, b.best_tile

def plot_scores(scores, best_tiles):

    # Plot the frequency of each unique element
    plt.hist(scores, bins=6)
    plt.title('scores')
    plt.xlabel('scores')
    plt.ylabel('Frequency')
    plt.show()

    best_dict = dict(sorted(Counter(best_tiles).items()))
    values, frequencies = best_dict.keys(), best_dict.values()
    value_names = [str(a) for a in values]
    # Plot the values and frequencies
    plt.bar(value_names, frequencies, align='center')
    plt.title('best_tiles')
    plt.xlabel('best_tiles')
    plt.ylabel('Frequency')
    plt.show()


def main():
    N = 4
    reps = 10000
    scores = []
    best_tiles = []

    for i in range(reps):
        b = game.Board(N)
        # print(f"game {i}: {b.score}")
        score, best_tile = game_run(b)
        scores.append(score)
        best_tiles.append(best_tile)

    plot_scores(scores, best_tiles)


if __name__ == "__main__":
    main()
# %%
