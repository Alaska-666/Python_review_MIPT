import argparse
import sys
import re
import pickle
import os
import collections
import os


def make_dictionary(words):
    dictionary = dict()
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        if word1 not in dictionary:
            dictionary[word1] = collections.Counter()
        dictionary[word1][word2] += 1
    return dictionary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '--input-dir', default='stdin',
                        help='Path to the directory with text')
    parser.add_argument('--model', default='model.txt', required=True,
                        help='Model save location')
    parser.add_argument('--lc', default=False,
                        help='To do or not to do lowercase')
    args = parser.parse_args()
    words = []
    if args.input == 'stdin':
        for line in sys.stdin.readlines():
            if args.lc:
                line = line.lower()
            words += re.findall(r'[A-Za-zА-Яа-я0-9]+|[.?,!@%"()]+', line)
        with open(args.model, 'wb') as f:
            pickle.dump(make_dictionary(words), f)
    else:
        txt_file = list(filter(lambda x: x.endswith('.txt'),
                               os.listdir(args.input)))
        for file in txt_file:
            file_path = os.path.join(args.input, file)
            with open(file_path, 'r') as f1:
                for line in f1:
                    if args.lc:
                        line = line.lower()
                    words += re.findall(r'[A-Za-zА-Яа-я0-9]+|[.?,!@%"()]+', line)
                with open(args.model, 'wb') as f:
                    pickle.dump(make_dictionary(words), f)


if __name__ == '__main__':
    main()
