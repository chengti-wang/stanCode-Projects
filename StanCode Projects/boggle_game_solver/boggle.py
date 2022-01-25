# DICTIONARY VERSION

# """
# File: boggle.py
# Name:
# ----------------------------------------
# TODO:
# """
#
# import time
# from sys import exit
#
# # This is the file name of the dictionary txt file
# # we will be checking if a word exists by searching through it
# FILE = 'dictionary.txt'
# ROWS = 4
#
# word_dict = {}
#
# class TrieNode:
# 	def __init__(self):
# 		self.children = {}
# 		self.end = False
#
#
# class Trie:
# 	def __init__(self):
# 		self.root = TrieNode()
#
# 	def insert(self, word):
# 		cur = self.root
# 		for ch in word:
# 			if ch not in cur.children:
# 				cur.children[ch] = TrieNode()
# 				cur = cur.children[ch]
# 			else:
# 				cur = cur.children[ch]
#
# 	def search(self, word):
# 		cur = self.root
# 		for ch in word:
# 			if ch not in cur.children:
# 				return False
# 			cur = cur.children[ch]
# 		return cur.end
#
#
# def main():
# 	"""
# 	TODO:
# 	"""
#
# 	#input
# 	letters = []
# 	for i in range(ROWS):
# 		string = input(f"{i+1} row of letters: ").replace(" ", "")
# 		if len(string) != ROWS:
# 			print("Illegal input")
# 			exit(0)
# 		letters.append(string)
#
# 	start = time.time()
# 	d = {}
# 	read_dictionary(d)
# 	for i in range(ROWS):
# 		for j in range(ROWS):
# 			find_words(letters, letters[i][j], i, j, -1, -1, d)
# 	print(f"There are {len(word_dict)} in total")
# 	end = time.time()
# 	print('----------------------------------')
# 	print(f'The speed of your boggle algorithm: {end - start} seconds.')
#
#
# def read_dictionary(d):
# 	"""
# 	This function reads file "dictionary.txt" stored in FILE
# 	and appends words in each line into a Python list
# 	"""
# 	with open(FILE, "r") as f:
# 		for line in f:
# 			line = line.strip()
# 			if len(line) >= 4:
# 				if line[0] in d:
# 					d[line[0]].append(line)
# 				else:
# 					d[line[0]] = [line]
#
#
#
# def find_words(letters, current_s, row, col, prev_row, prev_col, d):
# 	# print(current_s)
# 	if len(current_s) >= 4 and current_s in d[current_s[0]]:
# 		if current_s not in word_dict:
# 			print(f"Found:  {current_s}")
# 			word_dict[current_s] = 0
# 	if not has_prefix(current_s, d):
# 		return 0
# 	else:
# 		for i in [-1, 0, 1]:
# 			for j in [-1, 0, 1]:
# 				if 0 <= row+i < ROWS and 0 <= col+j < ROWS and not (i == 0 and j == 0) and not (row+i == prev_row and col+j ==prev_col):
# 					current_s += letters[row+i][col+j]
# 					find_words(letters, current_s, row+i, col+j, row, col, d)
# 					current_s = current_s[:-1]
#
#
# def has_prefix(sub_s, d):
# 	"""
# 	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
# 	:return: (bool) If there is any words with prefix stored in sub_s
# 	"""
# 	for key in d[sub_s[0]]:
# 		if key.startswith(sub_s):
# 			return True
#
#
#
# if __name__ == '__main__':
# 	main()
#
#
# """
# f y c l
# i o m g
# o r i l
# h j h u
# """


# TRIE VERSION

"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time
from sys import exit

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
ROWS = 4

word_dict = {}


class TrieNode:
	def __init__(self):
		self.children = {}
		self.end = False


class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		cur = self.root
		for ch in word:
			if ch not in cur.children:
				cur.children[ch] = TrieNode()
				cur = cur.children[ch]
			else:
				cur = cur.children[ch]
		cur.end = True

	def search(self, word):
		cur = self.root
		for ch in word:
			if ch not in cur.children:
				return False
			cur = cur.children[ch]
		return cur.end

	def startswith(self, word):
		cur = self.root
		for ch in word:
			if ch not in cur.children:
				return False
			cur = cur.children[ch]
		return True

def main():
	"""
	TODO:
	"""

	#input
	letters = []
	for i in range(ROWS):
		string = input(f"{i+1} row of letters: ").replace(" ", "")
		if len(string) != ROWS:
			print("Illegal input")
			exit(0)
		letters.append(string)

	start = time.time()
	d = Trie()
	read_dictionary(d)
	for i in range(ROWS):
		for j in range(ROWS):
			find_words(letters, letters[i][j], i, j, -1, -1, d)
	print(f"There are {len(word_dict)} in total")
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary(d):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, "r") as f:
		for line in f:
			line = line.strip()
			if len(line) >= 4:
				d.insert(line)


def find_words(letters, current_s, row, col, prev_row, prev_col, d):
	# print(current_s)
	if len(current_s) >= 4 and d.search(current_s):
		if current_s not in word_dict:
			print(f"Found:  {current_s}")
			word_dict[current_s] = 0
	if not d.startswith(current_s):
		return 0
	else:
		for i in [-1, 0, 1]:
			for j in [-1, 0, 1]:
				if 0 <= row+i < ROWS and 0 <= col+j < ROWS and not (i == 0 and j == 0) and not (row+i == prev_row and col+j ==prev_col):
					current_s += letters[row+i][col+j]
					find_words(letters, current_s, row+i, col+j, row, col, d)
					current_s = current_s[:-1]


def has_prefix(sub_s, d):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for key in d[sub_s[0]]:
		if key.startswith(sub_s):
			return True



if __name__ == '__main__':
	main()


"""
f y c l
i o m g
o r i l 
h j h u
"""