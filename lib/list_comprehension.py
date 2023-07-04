#!/usr/bin/env python3







newList = []
def return_evens(num_list):
    for n in num_list:
        if n % 2 == 0:
            newList.append(n)
    return newList



def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]