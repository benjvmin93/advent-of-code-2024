INPUT_PATH = "./input.csv"



def main():
    left_list = []
    right_list = []
    with open(INPUT_PATH, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    result = 0
    for elt in left_list:
        result += elt * right_list.count(elt)
    print(result)
    return result
    
if __name__ == "__main__":
    main()