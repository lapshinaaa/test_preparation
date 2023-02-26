def swap_nodes_in_pairs(list_of_nodes: list) -> list:
    if len(list_of_nodes) == 0 or len(list_of_nodes) == 1:  # base case
        return list_of_nodes

    else:   # general (recursive) case
        first_two = [list_of_nodes[1], list_of_nodes[0]]
        return first_two + swap_nodes_in_pairs(list_of_nodes[2:])


print(swap_nodes_in_pairs(list(map(int, input().split()))))
