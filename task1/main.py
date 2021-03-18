def slice_less(my_list, lesser):
    if type(my_list) != list or type(lesser) != int or not (all(isinstance(value, int) for value in my_list)):
        raise TypeError
    resulting_list = [value for value in my_list if value > lesser]
    return sorted(resulting_list, reverse=True)
