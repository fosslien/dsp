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





def front_x(words):
    nlist = []
    for word in words:
        if word[:1] == "x":
            nlist.append(word)
    nwords = [word for word in words if word not in nlist]
    sortednlist = sorted(nlist)
    sortednwords = sorted(nwords)
    print sortednlist + sortednwords

input = raw_input("Enter a bunch of words: ")
words = list(input.split())
front_x(words)




from ast import literal_eval

def sort_last(tuples):
    print sorted(tuples, key=lambda x: x[1])

tuples = literal_eval(raw_input("Please enter the data: "))
sort_last(tuples)


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

