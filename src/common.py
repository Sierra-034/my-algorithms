
def read_stdin_lines():
    try:
        while True:
            line = input().split()
            if not line: break
            yield line
    except EOFError:
        return

def prepare_binary_tree_data():
    for line in read_stdin_lines():
        return line
