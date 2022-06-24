
lst = [1, 2, 3, [1, 2, [1, 2], [4, [5, [6, [4]]], [3, 1]]]]
flatten = lambda lst: isinstance(lst, (int)) and [lst] or sum(map(flatten, lst), [])

flat_list = flatten(lst)
print(flat_list)
print(sum(flat_list))
