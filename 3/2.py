INPUT_PATH = "./input"

import re

def main():
    data = None
    with open(INPUT_PATH, 'r') as f:
        data = f.read()
    
    res = re.findall("(do)\(\)|mul\((\d{1,3}),(\d{1,3})\)|(don't)\(\)", data)
    
    enabled = True
    sum = 0
    for do, a, b, dont in res:
        if do:
            enabled = True
        elif dont:
            enabled = False
        else:
            if enabled:
                sum += int(a) * int(b)
    print(sum)
    return sum

if __name__ == "__main__":
    main()
    
    