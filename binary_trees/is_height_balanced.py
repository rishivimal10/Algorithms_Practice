def is_height_balanced_solution(binary_tree):

    if (find_height(binary_tree.left) - find_height(binary_tree.right)) < -1 or (find_height(binary_tree.left) - find_height(binary_tree.right)) > 1:
        return False

    return True


def find_height(binary_tree):

    if not binary_tree:
        return -1

    else:
        left_depth = find_height(binary_tree.left)
        right_depth = find_height(binary_tree.right)

    return max(left_depth+1, right_depth+1)



