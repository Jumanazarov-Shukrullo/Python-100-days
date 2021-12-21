class dotdict(dict):
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)


def win_loss_draw(score):
    if score > 0:
        return 'win'
    if score < 0:
        return 'loss'
    return 'draw'


"""
split one list to multiple lists
"""
split_group = lambda the_list, group_size: zip(*(iter(the_list), ) * group_size)

import numpy as np
import json
from connect4_game import Connect4Game


def get_test_dataset():
    game = Connect4Game()
    test_dataset = []
    # with open("refmoves1k_kaggle") as f:
    with open("/home/user/PycharmProjects/ConnectX/benchmark/torch/AlphaZero/refmoves1k_kaggle") as f:

        for line in f:
            data = json.loads(line)

            board = data["board"]
            board = np.reshape(board, game.getBoardSize()).astype(int)
            board[np.where(board == 2)] = -1

            # find out how many moves are played to set the correct mark.
            ply = len([x for x in data["board"] if x > 0])
            if ply & 1:
                player = -1
            else:
                player = 1

            test_dataset.append({
                'board': board,
                'player': player,
                'move_score': data['move score'],
            })
    return test_dataset