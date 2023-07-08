#!/usr/bin/env python3


def return_evens(number_list):
    return[numb for numb in number_list if numb % 2 == 0]

result = return_evens([1, 2, 3, 4, 5, 6, 7, 8])
print(result)


# newList = []
# def return_evens(num_list):
#     for n in num_list:
#         if n % 2 == 0:
#             newList.append(n)
#     return newList


def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]