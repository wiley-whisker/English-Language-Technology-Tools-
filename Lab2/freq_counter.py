"""
Frequency counter for texts.

author: Wiley Matthews
"""

import sys
from typing import Dict
import re

TEXT_PATH = 'texts/'


def read_file(filename : str) -> str:
    text = ''
    with open(filename) as f:
        for line in f:
            text += line
    return text


def clean(text : str) -> str:
    text = re.sub(r'[.,]', '', text)
    return text


def freq(text : str) -> Dict[str, int]:
    text = clean(text)
    freq_dict = {}
    word_list = text.lower().split()
    word_set = set(word_list)
    for word in word_set:
        freq_dict[word] = word_list.count(word)
    return freq_dict


def sort_freqs(freqs : Dict[str, int]) -> Dict[str, int]:
    sorted_as_lst = sorted(freqs.items(), key=lambda x : x[1], reverse=True)
    sorted_as_dict = dict(sorted_as_lst)
    return sorted_as_dict


def to_file(freqs : Dict[str, int], fname) -> None:
    with open(fname, 'w') as f:
        for word in freqs.keys():
            f.write(word + " " + str(freqs[word]) + "\n")


def main():
    fname = sys.argv[1]
    fpath = TEXT_PATH + fname
    out_name = sys.argv[2]
    out_path = TEXT_PATH + out_name

    text = read_file(fpath)
    freqs = sort_freqs(freq(text))
    to_file(freqs, out_path)


if __name__ == '__main__':
    main()
