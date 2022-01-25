"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

anagram_dict = {}


def main():
    """
    TODO:
    """

    global anagram_dict
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")

    while True:
        anagram = input("Find anagrams for: ")
        if anagram == EXIT:
            break
        start = time.time()
        d = {}
        read_dictionary(d, anagram)

        # NO RECURSION VERSION
        # print([word for word in d if sorted(word) == sorted(anagram)])

        # RECURSION VERSION
        print("Searching...")  # print searching for the first for loop
        find_anagrams(anagram, len(anagram), '', d)
        print(list(anagram_dict.keys()))
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')
        anagram_dict.clear()


def read_dictionary(d, string):

    with open(FILE, "r") as f:
        for line in f:
            line = line.strip()
            if len(line) == len(string):
                quit_ = False
                for letter in line:

                    if string.find(letter) == -1:
                        # print(f"{line} {letter}: {line.find(letter)}")
                        quit_ = True
                        break
                if not quit_:
                    d[line] = 0


def find_anagrams(s, target_length, current_s, d):
    """
    :param anagram_list:
    :param current_s:
    :param target_length:
    :param s:
    :return:
    """
    if len(current_s) == target_length:
        if current_s in d and current_s not in anagram_dict:
            print(f"Found:  {current_s}")
            print("Searching...")
            anagram_dict[current_s] = 0
    else:
        for letter in s:
            if current_s.count(letter) < s.count(letter):
                current_s += letter
                # if has_prefix(current_s, d):
                find_anagrams(s, target_length, current_s, d)
                current_s = current_s[:-1]


def has_prefix(sub_s, d):
    """
    :param sub_s:
    :return:
    """
    for key in d:
        if key.startswith(sub_s):
            return True


if __name__ == '__main__':
    main()
