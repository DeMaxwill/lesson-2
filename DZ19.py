
lst = [1, 2, 3, [1, 2, [1, 2], [4, [5, [6, [4]]], [3, 1]]]]
flatten = lambda lst: isinstance(lst, (int)) and [lst] or sum(map(flatten, lst), [])

flat_list = flatten(lst)

fl = [flat_list[i:i + 2] for i in range(0, len(flat_list), 2)]
print(len(fl) + len(flat_list))

