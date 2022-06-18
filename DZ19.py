def flatten(s):
    if s == []:
        return s
    if isinstance(s[0], list):
        return(flatten(s[0]) + flatten(s[1:]))
    return(s[:1] + flatten(s[1:]))
s = [1,2,3, [1,2,[1,2], [4, [5,[6, [4]]], [3, 1]]]]
print(flatten(s))
print(sum(flatten(s)))
