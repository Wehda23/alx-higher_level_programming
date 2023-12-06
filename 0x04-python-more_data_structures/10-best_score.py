#!/usr/bin/python3
def best_score(a_dictionary):
    score = None
    name = None
    if a_dictionary:
        score = 0
        for key, value in a_dictionary.items():
            if value > score:
                score = value
                name = key
    return name
