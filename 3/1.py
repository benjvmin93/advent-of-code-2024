INPUT_PATH = "./input"

import re

def main():
    data = None
    with open(INPUT_PATH, 'r') as f:
        data = f.read()
    
    res = re.findall("mul\(([0-9]+,[0-9]+)\)", data)
    
    print(res)
    sum = 0
    for x in res:
        numbers = x.split(',')
        sum += int(numbers[0]) * int(numbers[1])     
    print(sum)
    
    return sum
    
        
    

if __name__ == "__main__":
    main()
    
    