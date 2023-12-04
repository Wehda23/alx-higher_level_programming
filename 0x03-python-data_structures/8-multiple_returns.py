#!/usr/bin/python3
def multiple_returns(sentence):
    first = sentence[0] or None
    return (len(sentence), first)
