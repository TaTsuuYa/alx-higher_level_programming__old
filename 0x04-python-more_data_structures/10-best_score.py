#!/usr/bin/python3

def best_score(a_dictionary):
    key = None
    if not a_dictionary:
        return None

    score = list(a_dictionary.values())[0]
    for k, e in a_dictionary.items():
        if e > score:
            score = e
            key = k
    return key
