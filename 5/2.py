from collections import defaultdict, deque

def parse_input(file_path):
    rules = defaultdict(set)
    update_orders = []

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if "|" in line:
                page1, page2 = map(int, line.split("|"))
                rules[page1].add(page2)
            else:
                update_orders.append(list(map(int, line.split(","))))

    return rules, update_orders

def is_well_ordered(rules, update_order):
    page_positions = {page: i for i, page in enumerate(update_order)}
    for page1, dependencies in rules.items():
        for page2 in dependencies:
            if page1 in page_positions and page2 in page_positions:
                if page_positions[page1] > page_positions[page2]:
                    return False
    return True

def topological_sort_util(node, graph, visited, stack):
    """
    A recursive helper function for topological sorting.
    Stops recursing if the node is already visited.
    """
    # Base condition: if already visited, stop recursion
    if visited[node]:
        return

    # Mark the current node as visited
    visited[node] = True

    # Recur for all adjacent vertices (dependencies)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            topological_sort_util(neighbor, graph, visited, stack)

    # Add the current node to the stack after visiting all dependencies
    stack.append(node)


def topological_sort(rules, update):
    """
    Perform a topological sort on the graph represented by rules,
    restricted to the nodes in the update list.

    Parameters:
    - rules: dict, adjacency list representing the graph.
    - update: list, list of pages to be ordered.

    Returns:
    - List of nodes in topologically sorted order.
    """
    # Build the graph restricted to the update nodes
    graph = defaultdict(list)
    for page1, dependencies in rules.items():
        if page1 in update:
            for page2 in dependencies:
                if page2 in update:
                    graph[page1].append(page2)

    # Initialize visited dictionary and stack for the sort
    visited = {node: False for node in update}
    stack = []

    # Perform the recursive topological sort for each node in the update list
    for node in update:
        if not visited[node]:  # Only process unvisited nodes
            topological_sort_util(node, graph, visited, stack)

    # Return the reversed stack as the sorted order
    return stack[::-1]



def test():
    # Define test rules and updates
    rules = {
        47: {53},
        97: {13, 61, 47, 75, 29, 53},
        75: {29, 53, 47, 61, 13},
        61: {13, 53, 29},
        53: {29},
        29: {13},
    }
    test_updates = [
        [75, 97, 47, 61, 53],  # Needs reordering
        [61, 13, 29],          # Needs reordering
        [97, 13, 75, 29, 47],  # Needs reordering
        [75, 47, 61, 53, 29],  # Already well-ordered
    ]
    expected_results = [
        [97, 75, 47, 61, 53],
        [61, 29, 13],
        [97, 75, 47, 29, 13],
        [75, 47, 61, 53, 29],  # Should remain unchanged
    ]

    # Run tests
    for i, update in enumerate(test_updates):
        if is_well_ordered(rules, update):
            print(f"Test {i+1}: Update is already well-ordered as {update}.")
            assert update == expected_results[i], f"Test {i+1} failed!"
        else:
            corrected_update = topological_sort(rules, update)
            print(f"Test {i+1}: Corrected update {corrected_update}.")
            assert corrected_update == expected_results[i], f"Test {i+1} failed!"

    print("All tests passed!")

def main():
    test()
    INPUT_PATH = "./input"
    rules, update_orders = parse_input(INPUT_PATH)

    total = 0
    for update in update_orders:
        if not is_well_ordered(rules, update):
            # Add the middle page of the well-ordered update
            corrected_update = topological_sort(rules, update)
            total += corrected_update[len(corrected_update) // 2]

    print(f"Sum of middle pages after correcting: {total}")

if __name__ == "__main__":
    main()
