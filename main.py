import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class Tree:
    def __init__(self, cell_index, size, is_mine, is_dormant):
        self.cell_index = cell_index
        self.size = size
        self.is_mine = is_mine
        self.is_dormant = is_dormant


def sort_trees(tree):
    return tree.size + cells[tree.cell_index]


def calculate_move(trees):
    my_trees = [t for t in trees if t.is_mine == 1]
    my_trees.sort(reverse=True, key=sort_trees)
    return 'COMPLETE ' + str(my_trees[0].cell_index)


number_of_cells = int(input())  # 37

cells = []

for i in range(number_of_cells):
    # index: 0 is the center cell, the next cells spiral outwards
    # richness: 0 if the cell is unusable, 1-3 for usable cells
    # neigh_0: the index of the neighbouring cell for each direction
    index, richness, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]
    cells.insert(index, richness)

# game loop
while True:
    day = int(input())  # the game lasts 24 days: 0-23
    nutrients = int(input())  # the base score you gain from the next COMPLETE action
    # sun: your sun points
    # score: your current score
    sun, score = [int(i) for i in input().split()]
    inputs = input().split()
    opp_sun = int(inputs[0])  # opponent's sun points
    opp_score = int(inputs[1])  # opponent's score
    opp_is_waiting = inputs[2] != "0"  # whether your opponent is asleep until the next day
    number_of_trees = int(input())  # the current amount of trees

    trees = []
    for i in range(number_of_trees):
        inputs = input().split()
        cell_index = int(inputs[0])  # location of this tree
        size = int(inputs[1])  # size of this tree: 0-3
        is_mine = inputs[2] != "0"  # 1 if this is your tree
        is_dormant = inputs[3] != "0"  # 1 if this tree is dormant
        trees.insert(cell_index, Tree(cell_index, size, is_mine, is_dormant))
    number_of_possible_moves = int(input())
    possible_moves = []
    for i in range(number_of_possible_moves):
        possible_move = input()
        possible_moves.insert(i, possible_move)

    print(possible_moves, file=sys.stderr, flush=True)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # GROW cellIdx | SEED sourceIdx targetIdx | COMPLETE cellIdx | WAIT <message>
    if len(possible_moves) == 1:
        print(possible_moves[0])
    else:
        move = calculate_move(trees)
        print(move)