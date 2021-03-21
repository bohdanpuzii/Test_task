def slice_less(my_list, lesser):
    list_is_valid = type(my_list) == list
    list_items_are_valid = (all(isinstance(value, int) for value in my_list))
    lesser_is_valid = type(lesser) == int
    if not list_is_valid or not list_items_are_valid or not lesser_is_valid:
        raise TypeError('Given type is not supported')
    resulting_list = [value for value in my_list if value > lesser]
    return sorted(resulting_list, reverse=True)
