INPUT_PATH = "./input.csv"

def total_distance(left_list, right_list):
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
    return distance

def main():
    left_list = []
    right_list = []
    with open(INPUT_PATH, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    result = total_distance(left_list, right_list)
    print(result)
    return result

if __name__ == "__main__":
    main()