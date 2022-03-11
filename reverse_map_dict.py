# Reverse Dictionary mapping

ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
# Expected Output: {65: 'A', 66: 'B', 67: 'C', 68: 'D'}


# zip() returns a zip object, which is an iterator of tuples
# where the items in each passed iterators are paired together
def rev_map(d):
    d = dict(zip(d.values(), d.keys()))
    return d

# dict comprehension
def reverse_map(d):
    new_dict = {value: key for key, value in d.items()}
    return new_dict

print(rev_map(ascii_dict))
print(reverse_map(ascii_cict))
