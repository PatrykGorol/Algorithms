def look_for_a_key(main_box: list) -> None:
    pile = main_box
    while len(pile):
        print(f'pile: {pile}')
        print(f'current item: {pile[-1]}\n')
        item = pile.pop()
        if item == 'key':
            print('Found a key!')
            return None
        if isinstance(item, list):
            pile.extend(item)
    return None


def look_for_a_key_recursively(main_box: list) -> None:
    for item in main_box:
        if item == 'key':
            print('Found a key!')
            exit()
        if isinstance(item, list):
            look_for_a_key_recursively(item)
        else:
            print(item)
    return None


if __name__ == '__main__':
    s1 = ['doll', 'pony']
    s2 = ['key', 'treasure map']
    s3 = ['letter']
    s4 = ['shoes', 'socks']
    s5 = ['photos', 'old camera', 'photo album']
    m1 = [s1, s3, s4]
    m2 = ['video game', 'poster']
    m3 = [s2, ]
    m4 = [s5, ]
    l1 = [m1, m2]
    l2 = [m3, m4]
    l3 = ['old books']
    main_box = [l1, l2, l3]

    look_for_a_key(main_box)
    look_for_a_key_recursively(main_box)
