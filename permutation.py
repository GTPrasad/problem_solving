import itertools


# Using Iter package
def using_iter(s):
    nums = list(s)
    perm = list(itertools.permutations(nums))
    print(len([''.join(permutation) for permutation in perm]))


def swap(string, i, j):
    temp = string[i]
    string[i] = string[j]
    string[j] = temp


# Recursive function to print all permutations of a string
def permutations(ch, current_index=0):
    if current_index == len(ch) - 1:
        print(''.join(ch))

    for i in range(current_index, len(ch)):
        swap(ch, current_index, i)
        permutations(ch, current_index + 1)
        swap(ch, current_index, i)
