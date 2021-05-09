import copy
import sys
import math

distance_seedable_cells = [
    # Index 0
    [
        # Size 1
        [1, 2, 3, 4, 5, 6],
        # Size 2
        [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        # Size 3
        [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36],
    ],
    # Index 1
    [
        # Size 1
        [0, 2, 6, 7, 8, 18],
        # Size 2
        [3, 4, 5, 9, 10, 16, 17, 19, 20, 21, 35, 36],
        # Size 3
        [11, 12, 13, 14, 15, 22, 23, 24, 32, 33, 34],
    ],
    # Index 2
    [
        # Size 1
        [0, 1, 3, 8, 9, 10],
        # Size 2
        [4, 5, 6, 7, 11, 12, 18, 20, 21, 22, 23, 24],
        # Size 3
        [13, 14, 15, 16, 17, 19, 25, 26, 27, 35, 36],
    ],
    # Index 3
    [
        # Size 1
        [0, 2, 4, 10, 11, 12],
        # Size 2
        [1, 5, 6, 8, 9, 13, 14, 23, 24, 25, 26, 27],
        # Size 3
        [7, 15, 16, 17, 18, 20, 21, 22, 28, 29, 30],
    ],
    # Index 4
    [
        # Size 1
        [0, 3, 5, 12, 13, 14],
        # Size 2
        [1, 2, 6, 10, 11, 15, 16, 26, 27, 28, 29, 30],
        # Size 3
        [7, 8, 9, 17, 18, 23, 24, 25, 31, 32, 33],
    ],
    # Index 5
    [
        # Size 1
        [0, 4, 6, 14, 15, 16],
        # Size 2
        [1, 2, 3, 12, 13, 17, 18, 29, 30, 31, 32, 33],
        # Size 3
        [7, 8, 9, 10, 11, 26, 27, 28, 34, 35, 36],
    ],
    # Index 6
    [
        # Size 1
        [0, 1, 5, 16, 17, 18],
        # Size 2
        [2, 3, 4, 7, 8, 14, 15, 32, 33, 34, 35, 36],
        # Size 3
        [9, 10, 11, 12, 13, 19, 20, 21, 29, 30, 31],
    ],
    # Index 7
    [
        # Size 1
        [1, 8, 18, 19, 20, 36],
        # Size 2
        [0, 2, 6, 9, 17, 21, 35],
        # Size 3
        [3, 4, 5, 10, 16, 22, 23, 33, 34],
    ],
    # Index 8
    [
        # Size 1
        [1, 2, 7, 9, 20, 21],
        # Size 2
        [0, 3, 6, 10, 18, 19, 22, 23, 36],
        # Size 3
        [4, 5, 11, 12, 16, 17, 24, 35],
    ],
    # Index 9
    [
        # Size 1
        [2, 8, 10, 21, 22, 23],
        # Size 2
        [0, 1, 3, 7, 11, 20, 24],
        # Size 3
        [4, 5, 6, 12, 18, 19, 25, 26, 36],
    ],
    # Index 10
    [
        # Size 1
        [2, 3, 9, 11, 23, 24],
        # Size 2
        [0, 1, 4, 8, 12, 21, 22, 25, 26],
        # Size 3
        [5, 6, 7, 13, 14, 18, 20, 27],
    ],
    # Index 11
    [
        # Size 1
        [3, 10, 12, 24, 25, 26],
        # Size 2
        [0, 2, 4, 9, 13, 23, 27],
        # Size 3
        [1, 5, 6, 8, 14, 21, 22, 28, 29],
    ],
    # Index 12
    [
        # Size 1
        [3, 4, 11, 13, 26, 27],
        # Size 2
        [0, 2, 5, 10, 14, 24, 25, 28, 29],
        # Size 3
        [1, 6, 8, 9, 15, 16, 23, 30],
    ],
    # Index 13
    [
        # Size 1
        [4, 12, 14, 27, 28, 29],
        # Size 2
        [0, 3, 5, 11, 15, 26, 30],
        # Size 3
        [1, 2, 6, 10, 16, 24, 25, 31, 32],
    ],
    # Index 14
    [
        # Size 1
        [4, 5, 13, 15, 29, 30],
        # Size 2
        [0, 3, 6, 12, 16, 27, 28, 31, 32],
        # Size 3
        [1, 2, 10, 11, 17, 18, 26, 33],
    ],
    # Index 15
    [
        # Size 1
        [5, 14, 16, 30, 31, 32],
        # Size 2
        [0, 4, 6, 13, 17, 29, 33],
        # Size 3
        [1, 2, 3, 12, 18, 27, 28, 34, 35],
    ],
    # Index 16
    [
        # Size 1
        [5, 6, 15, 17, 32, 33],
        # Size 2
        [0, 1, 4, 14, 18, 30, 31, 34, 35],
        # Size 3
        [2, 3, 7, 8, 12, 13, 29, 36],
    ],
    # Index 17
    [
        # Size 1
        [6, 16, 18, 33, 34, 35],
        # Size 2
        [0, 1, 5, 7, 15, 32, 36],
        # Size 3
        [2, 3, 4, 8, 14, 19, 20, 30, 31],
    ],
    # Index 18
    [
        # Size 1
        [1, 6, 7, 17, 35, 36],
        # Size 2
        [0, 2, 5, 8, 16, 19, 20, 33, 34],
        # Size 3
        [3, 4, 9, 10, 14, 15, 21, 32],
    ],
    # Index 19
    [
        # Size 1
        [7, 20, 36],
        # Size 2
        [1, 8, 18, 21, 35],
        # Size 3
        [0, 2, 6, 9, 17, 22, 34],
    ],
    # Index 20
    [
        # Size 1
        [7, 8, 19, 21],
        # Size 2
        [1, 2, 9, 18, 22, 36],
        # Size 3
        [0, 3, 6, 10, 17, 23, 35],
    ],
    # Index 21
    [
        # Size 1
        [8, 9, 20, 22],
        # Size 2
        [1, 2, 7, 10, 19, 23],
        # Size 3
        [0, 3, 6, 11, 18, 24, 36],
    ],
    # Index 22
    [
        # Size 1
        [9, 21, 23],
        # Size 2
        [2, 8, 10, 20, 24],
        # Size 3
        [0, 1, 3, 7, 11, 19, 25],
    ],
    # Index 23
    [
        # Size 1
        [9, 10, 22, 24],
        # Size 2
        [2, 3, 8, 11, 21, 25],
        # Size 3
        [0, 1, 4, 7, 12, 20, 26],
    ],
    # Index 24
    [
        # Size 1
        [10, 11, 23, 25],
        # Size 2
        [2, 3, 9, 12, 22, 26],
        # Size 3
        [0, 1, 4, 8, 13, 21, 27],
    ],
    # Index 25
    [
        # Size 1
        [11, 24, 26],
        # Size 2
        [3, 10, 12, 23, 27],
        # Size 3
        [0, 2, 4, 9, 13, 22, 28],
    ],
    # Index 26
    [
        # Size 1
        [11, 12, 25, 27],
        # Size 2
        [3, 4, 10, 13, 24, 28],
        # Size 3
        [0, 2, 5, 9, 14, 23, 29],
    ],
    # Index 27
    [
        # Size 1
        [12, 13, 26, 28],
        # Size 2
        [3, 4, 11, 14, 25, 29],
        # Size 3
        [0, 2, 5, 10, 15, 24, 30],
    ],
    # Index 28
    [
        # Size 1
        [13, 27, 29],
        # Size 2
        [4, 12, 14, 26, 30],
        # Size 3
        [0, 3, 5, 11, 15, 25, 31],
    ],
    # Index 29
    [
        # Size 1
        [13, 14, 28, 30],
        # Size 2
        [4, 5, 12, 15, 27, 31],
        # Size 3
        [0, 3, 6, 11, 16, 26, 32],
    ],
    # Index 30
    [
        # Size 1
        [14, 15, 29, 31],
        # Size 2
        [4, 5, 13, 16, 28, 32],
        # Size 3
        [0, 3, 6, 12, 17, 27, 33],
    ],
    # Index 31
    [
        # Size 1
        [15, 30, 32],
        # Size 2
        [5, 14, 16, 29, 33],
        # Size 3
        [0, 4, 6, 13, 17, 28, 34],
    ],
    # Index 32
    [
        # Size 1
        [15, 16, 31, 33],
        # Size 2
        [5, 6, 14, 17, 30, 34],
        # Size 3
        [0, 1, 4, 13, 18, 29, 35],
    ],
    # Index 33
    [
        # Size 1
        [16, 17, 32, 34],
        # Size 2
        [5, 6, 15, 18, 31, 35],
        # Size 3
        [0, 1, 4, 7, 14, 30, 36],
    ],
    # Index 34
    [
        # Size 1
        [17, 33, 35],
        # Size 2
        [6, 16, 18, 32, 36],
        # Size 3
        [0, 1, 5, 7, 15, 19, 31],
    ],
    # Index 35
    [
        # Size 1
        [17, 18, 34, 36],
        # Size 2
        [1, 6, 7, 16, 19, 33],
        # Size 3
        [0, 2, 5, 8, 15, 20, 32],
    ],
    # Index 36
    [
        # Size 1
        [7, 18, 19, 35],
        # Size 2
        [1, 6, 8, 17, 20, 34],
        # Size 3
        [0, 2, 5, 9, 16, 21, 33],
    ],
]


class Tree:
    def __init__(self, cell_index, size, is_mine, is_dormant):
        self.cell_index = cell_index
        self.size = size
        self.is_mine = is_mine
        self.is_dormant = is_dormant

    def __eq__(self, other):
        return self.cell_index == other.cell_index

    def sleep(self):
        self.is_dormant = True

    def grow(self):
        self.size += 1
        self.is_dormant = True


class Cell:
    def __init__(self, index, richness, neighbors):
        self.index = index
        self.richness = richness
        self.neighbors = neighbors


class State:
    def __init__(self, day, nutrient, sun, score, opp_sun, opp_score, opp_is_waiting, number_of_trees, trees, action, trees_size):
        self.trees_size = trees_size
        self.action = action
        self.trees = trees
        self.number_of_trees = number_of_trees
        self.opp_is_waiting = opp_is_waiting
        self.opp_score = opp_score
        self.opp_sun = opp_sun
        self.score = score
        self.sun = sun
        self.nutrient = nutrient
        self.day = day


class Node:
    def __init__(self, parent_node, state):
        self.state = state
        self.parent_node = parent_node
        self.children = []
        self.total_games = 0
        self.won_games = 0

    def uct_value(self):
        return (self.won_games / self.total_games) + math.sqrt(2) * math.sqrt((math.log2(self.parent_node.total_games)) / self.total_games)

    def add_child(self, state):
        self.children.append(Node(parent_node=self, state=state))


# TODO: Add shadow calculation
def create_children(node):
    # Add COMPLETE actions when possible
    if node.state.sun >= 4:
        trees_3 = [t for t in node.state.trees if t.size == 3 and not t.is_dormant and t.is_mine]
        for tree_3 in trees_3:
            new_state = copy.deepcopy(node.state)
            new_state.trees[tree_3.cell_index] = None
            new_state.score += cells[tree_3.cell_index].richness + new_state.nutrient
            new_state.nutrient -= 1
            new_state.sun -= 4
            new_state.sun += new_state.trees_size[3] * 3 + new_state.trees_size[2] * 2 + new_state.trees_size[1]
            new_state.action = f'COMPLETE {tree_3.cell_index}'
            node.add_child(new_state)

    # Add GROW to size 3 actions when possible
    if node.state.sun >= 7 + node.state.trees_size[3]:
        trees_2 = [t for t in node.state.trees if t.size == 2 and not t.is_dormant and t.is_mine]
        for tree_2 in trees_2:
            new_state = copy.deepcopy(node.state)
            new_state.trees[tree_2.cell_index].grow()
            new_state.sun -= (7 + node.state.trees_size[3])
            new_state.sun += new_state.trees_size[3] * 3 + new_state.trees_size[2] * 2 + new_state.trees_size[1]
            new_state.action = f'GROW {tree_2.cell_index}'
            node.add_child(new_state)

    # Add GROW to size 2 actions when possible
    if node.state.sun >= 3 + node.state.trees_size[2]:
        trees_1 = [t for t in node.state.trees if t.size == 1 and not t.is_dormant and t.is_mine]
        for tree_1 in trees_1:
            new_state = copy.deepcopy(node.state)
            new_state.trees[tree_1.cell_index].grow()
            new_state.sun -= (3 + node.state.trees_size[2])
            new_state.sun += new_state.trees_size[3] * 3 + new_state.trees_size[2] * 2 + new_state.trees_size[1]
            new_state.action = f'GROW {tree_1.cell_index}'
            node.add_child(new_state)

    # Add GROW to size 1 actions when possible
    if node.state.sun >= 1 + node.state.trees_size[1]:
        trees_0 = [t for t in node.state.trees if t.size == 0 and not t.is_dormant and t.is_mine]
        for tree_0 in trees_0:
            new_state = copy.deepcopy(node.state)
            new_state.trees[tree_0.cell_index].grow()
            new_state.sun -= (1 + node.state.trees_size[1])
            new_state.sun += new_state.trees_size[3] * 3 + new_state.trees_size[2] * 2 + new_state.trees_size[1]
            new_state.action = f'GROW {tree_0.cell_index}'
            node.add_child(new_state)

    # Add SEED actions when possible
    if node.state.sun >= node.state.trees_size[0]:
        cells_to_seed = []
        for tree in [t for t in node.state.trees if t is not None]:
            # Add a class method to test if a tree can be used
            if not tree.is_dormant and tree.is_mine:
                cells_indexes = distance_seedable_cells[tree.cell_index][tree.size - 1]
                for cell_index in cells_indexes:
                    if cells[cell_index].richness > 0 and node.state.trees[cell_index] is None:
                        cells_to_seed.append((tree.cell_index, cells[cell_index]))
        for (source_cell, target_cell) in cells_to_seed:
            print(node.state.trees, file=sys.stderr, flush=True)
            print(source_cell, file=sys.stderr, flush=True)
            new_state = copy.deepcopy(node.state)
            tree = Tree(cell_index=target_cell.index, size=0, is_mine=True, is_dormant=True)
            new_state.trees.insert(target_cell.index, tree)
            new_state.trees[source_cell].sleep()
            new_state.sun -= node.state.trees.size[0]
            node.add_child(new_state)

    return node


def mcts_selection(nodes):
    nodes.sort(reverse=True, key=Node.uct_value)
    return nodes[0]


def mcts_expansion():
    return


def mcts_simulation():
    return


def mcts_backpropagation():
    return


def find_best_choice(current_state):
    root = create_children(Node(parent_node=None, state=current_state))
    mcts_selection([root])
    mcts_expansion()
    mcts_simulation()
    mcts_backpropagation()
    return 'WAIT'


cells = []


def main():
    number_of_cells = int(input())  # 37
    for i in range(number_of_cells):
        # index: 0 is the center cell, the next cells spiral outwards
        # richness: 0 if the cell is unusable, 1-3 for usable cells
        # neigh_0: the index of the neighbouring cell for each direction
        index, richness, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]
        cells.append(Cell(index, richness, [c for c in (neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5) if c != -1]))

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

        trees = [None] * 37
        trees_size = [0, 0, 0, 0]
        for i in range(number_of_trees):
            inputs = input().split()
            cell_index = int(inputs[0])  # location of this tree
            size = int(inputs[1])  # size of this tree: 0-3
            is_mine = inputs[2] != "0"  # 1 if this is your tree
            is_dormant = inputs[3] != "0"  # 1 if this tree is dormant
            trees.insert(cell_index, Tree(cell_index, size, is_mine, is_dormant))
            if is_mine:
                trees_size[size] += 1

        current_state = State(day, nutrients, sun, score, opp_sun, opp_score, opp_is_waiting, number_of_trees, trees, None, trees_size)

        number_of_possible_moves = int(input())
        possible_moves = [input() for _ in range(number_of_possible_moves)]

        print(possible_moves, file=sys.stderr, flush=True)

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)

        # GROW cellIdx | SEED sourceIdx targetIdx | COMPLETE cellIdx | WAIT <message>
        if len(possible_moves) == 1:
            print(possible_moves[0])
        else:
            move = find_best_choice(current_state)
            print(move)


if __name__ == "__main__":
    main()
