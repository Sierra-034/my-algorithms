import pytest


@pytest.fixture
def load_data():
    def _load_data(file_path):
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    return _load_data

def test_example(load_data):
    data = load_data('./data/binary_tree.txt')
    assert data is not None
