def unhook_last_right_vertex_from_left(root):
    parent_node = root
    current_node = parent_node.left

    if not current_node:
        return None

    if not current_node.right:
        return current_node

    while current_node.right:
        parent_node = current_node
        current_node = parent_node.right

    parent_node.right = current_node.left
    current_node.left = None
    return current_node


def unhook_last_left_vertex_from_right(root):
    parent_node = root
    current_node = parent_node.right

    if not current_node:
        return None

    if not current_node.left:
        return current_node

    while current_node.left:
        parent_node = current_node
        current_node = parent_node.left

    parent_node.left = current_node.right
    current_node.right = None
    return current_node


def remove(root, key):
    parent_node = None
    current_node = root

    while current_node:
        if key < current_node.value:
            parent_node = current_node
            current_node = parent_node.left
        elif key > current_node.value:
            parent_node = current_node
            current_node = parent_node.right
        else:
            if current_node.left:
                # finding the rightmost vertex in the left tree
                new_node = unhook_last_right_vertex_from_left(current_node)
                new_node.right = current_node.right
                if current_node.left is not new_node:
                    new_node.left = current_node.left
            elif current_node.right:
                # finding the leftmost vertex in the right tree
                new_node = unhook_last_left_vertex_from_right(current_node)
                new_node.left = current_node.left
                if current_node.right is not new_node:
                    new_node.right = current_node.right
            else:
                if parent_node:
                    # removing a leaf of a tree without children
                    if key < parent_node.value:
                        parent_node.left = None
                    else:
                        parent_node.right = None
                    break
                else:
                    # deleting the root of a tree without children
                    return None

            current_node.left = None
            current_node.right = None

            if parent_node:
                # connecting the parent node to the new node
                if parent_node.left is current_node:
                    parent_node.left = new_node
                else:
                    parent_node.right = new_node
                break
            else:
                # when removing a root, we get a new root
                return new_node

    return root
