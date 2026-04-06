#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_key = None
    max_score = 0

    for key, value in a_dictionary.items():
        if best_key is None or value > max_score:
            max_score = value
            best_key = key
    return best_key
