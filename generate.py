import argparse
import sys
import re
import collections
import pickle
import random


def generator(word, lenght, model, output):
    with open(model, 'rb') as m:
        words = pickle.load(m, encoding='UTF-8')
    w = word
    for line in fileinput.input(output):
        line.write(w)
        line.write(' ')
    for i in range(lenght - 1):
        if w in list(words.keys()):
            s = 0
            for k in list(words[w].elements()):
                s += words[w][k]
            value = random.choice(range(1, s + 1))
            s = 0
            for k in list(words[w].elements()):
                s += words[w][k]
                if s >= value:
                    w = k
                    break
        else:
            w = random.choice(list(words.keys()))
            line.write(w)
            line.write(' ')

