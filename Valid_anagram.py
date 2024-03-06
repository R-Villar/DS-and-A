"""
Given two strings s1 and s2,
check if they're anagrams. Two strings are anagrams if they're made of the same characters with the same
frequencies.

Two strings are anagrams if they're made of the same characters with the same
frequencies.

freq1 = frequencies of
characters of s1
freq2 = frequencies of
characters of s2
freq1 == freq2 => s1 and s2 are
anagrams
"""
from collections import Counter


def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    freq1 = {}
    freq2 = {}

    for character in s1:
        if character in freq1:
            freq1[character] += 1
        else:
            freq1[character] = 1

    for character in s2:
        if character in freq2:
            freq2[character] += 1
        else:
            freq2[character] = 1
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
    return True


def are_anagrams2(s1, s2):
    if len(s1) != len(s2):
        return False

    return Counter(s1) == Counter(s2)


print(are_anagrams("glean", "angel"))
print(are_anagrams("Bored", "Robed"))
print(are_anagrams("dusty", "study"))
print(are_anagrams("dusty", "teacher"))

print(are_anagrams2("glean", "angel"))
print(are_anagrams2("Bored", "Robed"))
print(are_anagrams2("dusty", "study"))
