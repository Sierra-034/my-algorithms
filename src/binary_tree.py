from common import prepare_binary_tree_data

class TreeNode:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None


def create_level_order(lyst: list, position: int = 0, root: TreeNode = None):
    if position >= len(lyst) or not lyst[position]:
        return root

    root = TreeNode(lyst[position])
    root.left = create_level_order(lyst, 2 * position + 1, root.left)
    root.right = create_level_order(lyst, 2 * position + 2, root.right)
    return root

def inorder_traversal(node: TreeNode):
    if not node: return
    
    yield from inorder_traversal(node.left)
    yield node
    yield from inorder_traversal(node.right)

def get_node(value: int, tree: TreeNode) -> TreeNode:
    for item in inorder_traversal(tree):
        if item.data == value:
            return item

if __name__ == '__main__':
    lyst = prepare_binary_tree_data()
    tree = create_level_order(lyst)
