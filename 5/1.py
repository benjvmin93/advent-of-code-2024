def is_well_ordered(rules, update_order):
    """
    Check if the update_order is well-ordered according to the given rules.
    """
    n = len(update_order)
    for i in range(n):
        for j in range(i + 1, n):
            page1, page2 = update_order[i], update_order[j]
            # Check if the rule is violated
            if page2 not in rules.get(page1, set()) or page1 in rules.get(page2, set()):
                return False
    return True

def main():
    INPUT_PATH = "./input"
    rules = {}
    update_orders = []

    with open(INPUT_PATH, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if "|" in line:
                page1, page2 = line.split("|")
                if page1 not in rules:
                    rules[page1] = set()
                rules[page1].add(page2)
            else:
                update_orders.append(line.split(","))

    total = 0
    for update in update_orders:
        if is_well_ordered(rules, update):
            total += int(update[len(update) // 2])

    print(f"Sum of middle pages: {total}")

if __name__ == "__main__":
    main()
