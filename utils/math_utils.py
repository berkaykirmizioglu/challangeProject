def most_common(lst):
    return max(set(lst), key=lst.count)


def count_repeated_element(lst, x):
    return lst.count(x)
