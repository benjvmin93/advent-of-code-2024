import numpy as np
import os
import time


CHANGE_DIR_MATRIX = np.array([[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])
DIRECTIONS_BASE = [
        [-1, 0],
        [0, 1],
        [1, 0],
        [0, -1]
]

def update_pos(pos: tuple[int, int], direction: tuple[int, int]):
    p1, p2 = pos
    d1, d2 = direction
    return (p1 + d1, p2 + d2)

def rotate_direction(direction: list[int]):
    current_dir = np.zeros(4)
    current_dir[DIRECTIONS_BASE.index(direction)] = 1
    next_idx = CHANGE_DIR_MATRIX @ current_dir
    next_dir_vec = DIRECTIONS_BASE[list(next_idx).index(1)]
    return tuple(next_dir_vec)

def move(data, pos: tuple[int, int], direction: tuple[int, int], count):
    k, l = pos
    print(k, l)
    data[k][l] = "X"
    print_board(data)
    if k < 0 or l < 0 or k >= len(data) - 1 or l >= len(data[k]) - 1:
        return count

    (i, j) = update_pos(pos, direction)
    next_dir = direction
    if data[i][j] == "#":
        next_dir = rotate_direction(list(direction))
    return move(data, (i, j), next_dir, count + 1)

def test():
    data = [
        
    ]
    
def print_board(data):
    os.system('clear')
    for d in data:
        str = "".join(d)
        print(str, )
    time.sleep(0.05)


def main():
    INPUT_PATH = "./input"
    data = []
    initial_pos = (-1, -1)
    initial_direction = (-1, -1)
    directions = ['^', '>', 'v', '<']

    with open(INPUT_PATH, 'r') as f:
        while True:
            line = f.readline().strip()
            if line == "":
                break
            data.append([c for c in line])
            current_i = len(data) - 1
            for d in directions:
                if d in line:
                    print(f"FOUND THE CHARACTER!!")
                    initial_pos = (current_i, line.index(d))
                    initial_direction = DIRECTIONS_BASE[directions.index(d)]
    print(len(data), len(data[0]))
    if initial_pos == (-1, -1) or initial_direction == (-1, -1):
        raise Exception("OSKOUR")    
    i, j = initial_pos
    print(i, j)
    print_board(data)
    
    
    count = move(data, pos=initial_pos, direction=tuple(initial_direction), count=0)
    
    print(count)
    
            
if __name__ == "__main__":
    main()