def superset(set_a, set_b):
    if set_a >= set_b:
        return True
    else:
        return False


set_1 = {1, 2, 3, 4}
set_2 = {2, 3, 4, 5}

print(superset(set_1, set_2))