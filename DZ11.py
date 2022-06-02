import random
import string


def gen_rand_dict():
    dictionary = dict()
    while len(dictionary) < 10:
        rand_letter = random.choice(string.ascii_letters.lower())
        rand_number = random.randint(0, 9)
        dictionary.update({rand_letter: rand_number})
    return dictionary


def gen_new_dict(d_1, d_2):
    new_dict = d_1.copy()
    for key, value in d_1.items():
        for k, v in d_2.items():
            if k not in new_dict.keys() \
                    or (k == key and v > value):
                new_dict.update({k: v})
    return new_dict


dict_1 = gen_rand_dict()
dict_2 = gen_rand_dict()
dict_3 = gen_new_dict(dict_1, dict_2)

print(dict_1, dict_2, dict_3, sep='\n')