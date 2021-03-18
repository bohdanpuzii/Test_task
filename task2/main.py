def even_to_value(value_to_check, even):
    return True if value_to_check % even == 0 else False


def replace_even_3_5(start, end):
    for i in range(start, end + 1):
        if even_to_value(i, 3) and even_to_value(i, 5):
            print('$$@@')
        elif even_to_value(i, 3):
            print('$$')
        elif even_to_value(i, 5):
            print('@@')
        else:
            print(i)


if __name__ == '__main__':
    replace_even_3_5(11, 79)
