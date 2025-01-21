
def get_power_set(chars: str, indet = 0):
    debug_msg = '.' * indet + f'in get_power_set({chars})'
    print(f'{debug_msg}, start.')

    if chars == '':
        print(f'{debug_msg} base case returns [""]')
        return ['']
    
    # RECURSIVE CASE
    power_set = list()
    head = chars[0]
    tail = chars[1:]

    # First part, get the sets that don't include the head:
    print(f'{debug_msg} part 1 get sets without head "{head}"')
    tail_power_ser = get_power_set(tail, indet + 1)

    # Secodn part, get the sets that include the head:
    print(f'{debug_msg} part 2 get sets with head "{head}"')
    for tail_set in tail_power_ser:
        print(debug_msg, 'New set:', head + tail_set)
        power_set.append(head + tail_set)

    power_set = power_set + tail_power_ser
    print(debug_msg, 'returning:', power_set)
    return power_set

if __name__ == '__main__':
    print('the power set of ABC:')
    print(get_power_set('abc'))
