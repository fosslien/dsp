# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    total = 0
    for word in words:
        if len(word) > 1:
            if word[:1] == word [-1:]:
                total += 1
            else:
                total += 0
    print total


input = raw_input("Enter a bunch of words: ")
words = list(input.split())
match_ends(words)


def front_x(words):
    nlist = []
    for word in words:
        if word[:1] == "x":
            words.remove(word)
            nlist.append(word)
    sortedwords = sorted(words)
    sortednlist = sorted(nlist)
    print sortednlist
    print sortednlist + sortedwords






input = raw_input("Enter a bunch of words: ")
words = list(input.split())
front_x(words)
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    raise NotImplementedError


def sort_last(tuples):
    print sorted(tuples, key=lambda x: x[1])

input = raw_input("Enter a bunch of words: ")
tuples = tuple(map(int,input.split(',')))
sort_last(tuples)
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    raise NotImplementedError


def remove_adjacent(nums):
    i = 1
    while i < len(nums):
        if nums[i] == nums[i-1]:
            nums.pop(i)
            i -= 1
        i += 1
    print nums



input = raw_input("Enter a bunch of numbers: ")
nums = list(input.split())
remove_adjacent(nums)



def linear_merge(list1, list2):
    mergedlist = list1 + list2
    print sorted(mergedlist)


input1 = raw_input("Enter a bunch of words: ")
input2 = raw_input("Enter a bunch of words: ")
list1 = list(input1.split())
list2 = list(input2.split())
linear_merge(list1, list2)

