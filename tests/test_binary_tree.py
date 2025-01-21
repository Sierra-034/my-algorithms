from .test_common import load_data
from binary_tree import create_level_order, TreeNode

def test_create_level_order(load_data):
    lyst = load_data('./data/binary_tree.txt')
    tree = create_level_order(lyst.split())
    assert tree.data == 'a'
    assert tree.left.data == 'b'
    assert tree.right.data == 'c'
    assert tree.left.left.data == 'd'
    assert tree.left.right.data == 'e'
    assert tree.right.left.data == 'f'
    assert tree.right.right.data == 'g'
