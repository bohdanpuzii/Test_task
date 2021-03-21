def get_dictionary_by_value(value):
    result = {'$$@@': value % 3 == 0 and value % 5 == 0,
              '$$': value % 3 == 0,
              '@@': value % 5 == 0}
    return result


def get_first_true_key(dictionary):
    keys = dictionary.keys()
    for key in keys:
        if dictionary[key]:
            return key


def print_results_in_range(start, end):
    for value in range(start, end + 1):
        dictionary = get_dictionary_by_value(value)
        first_key = get_first_true_key(dictionary)
        print(first_key or value)


if __name__ == '__main__':
    print_results_in_range(11, 79)
