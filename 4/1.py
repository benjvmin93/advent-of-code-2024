def find_xmas_rec(data, i: list[int], j: list[int], xmas_str: str="") -> int:
    next_i = i.pop(0)
    next_j = j.pop(0)
    
    xmas_str += data[next_i][next_j]
    if xmas_str == "XMAS":
        return 1
    elif "XMAS".find(xmas_str) == -1:
        return 0
    else:
        return find_xmas_rec(data, i, j, xmas_str)

def find_xmas(data):
    count = 0
    len_xmas = len("XMAS")
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != "X":
                continue

            # Find vertical
            if i - len_xmas - 1 >= 0:
                count += find_xmas_rec(data, [k for k in range(i, i - len_xmas, -1)], [j for _ in range(len_xmas)])   # Going up
            if i + len_xmas < len(data):
                count += find_xmas_rec(data, [k for k in range(i, i + len_xmas)], [j for _ in range(len_xmas)])  # Going down

            # Find horizontal
            if j + len_xmas < len(data[i]):
                count += find_xmas_rec(data, [i for _ in range(len_xmas)], [k for k in range(j, j + len_xmas)])    # Going right
            if j - len_xmas - 1 >= 0:
                count += find_xmas_rec(data, [i for _ in range(len_xmas)], [k for k in range(j, j - len_xmas, -1)])    # Going left

            # Find diagonal
            if i - len_xmas - 1 >= 0 and j - len_xmas - 1 >= 0:
                count += find_xmas_rec(data, [k for k in range(i, i - len_xmas, -1)], [k for k in range(j, j - len_xmas, -1)])    # Going up left
            if i - len_xmas - 1 >= 0 and j + len_xmas < len(data[i]):
                count += find_xmas_rec(data, [k for k in range(i, i - len_xmas, -1)], [k for k in range(j, j + len_xmas)])    # Going up right
            if i + len_xmas < len(data) and j - len_xmas - 1 >= 0:
                count += find_xmas_rec(data, [k for k in range(i, i + len_xmas)], [k for k in range(j, j - len_xmas, -1)])    # Going down left
            if i + len_xmas < len(data) and j + len_xmas < len(data[i]):
                count += find_xmas_rec(data, [k for k in range(i, i + len_xmas)], [k for k in range(j, j + len_xmas)])    # Going down right

    return count

def main():
    INPUT_PATH = "./input"
    data: list[str] = None
    with open(INPUT_PATH, 'r') as f:
        data = f.readlines()
    
    count = find_xmas(data)
    print(count)
    
if __name__ == "__main__":
    main()