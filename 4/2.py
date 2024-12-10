def is_valid_index(data, i, j):
    return 0 <= i < len(data) and 0 <= j < len(data[i])

def find_mas(data, i, j):
    diag1 = [(-1, -1), (0, 0), (1, 1)]
    diag2 = [(1, -1), (0, 0), (-1, 1)]

    def extract_diagonal(offsets):
        return "".join(
            data[i + di][j + dj] if is_valid_index(data, i + di, j + dj) else ""
            for di, dj in offsets
        )

    return (
        extract_diagonal(diag1) in {"MAS", "SAM"}
        and extract_diagonal(diag2) in {"MAS", "SAM"}
    )

def find_x_mas(data):
    count = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            # Check only if the center is 'A'
            if data[i][j] == "A" and find_mas(data, i, j):
                count += 1
    return count

def main():
    INPUT_PATH = "./input"
    with open(INPUT_PATH, 'r') as f:
        data = [line.strip() for line in f.readlines()]  # Remove newlines

    count = find_x_mas(data)
    print(f"Number of X-MAS patterns: {count}")

if __name__ == "__main__":
    main()
