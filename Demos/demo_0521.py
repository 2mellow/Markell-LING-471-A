__author__ = 'Markell Thornton'
# TODO: Corpus terminologies
# "The cat chases the cat that was chasing the mouse."
# Type: the cat chase that was chasing mouse
# Token: the: 3; cat 2; chases: 1 that: 1; was:1; chasing: 1; mouse: 1
# Hapax legomenon: chases, that, was, chasing, mouse
# Wordform: chases, chasing
# Lemma: chase
sentence = "The cat chases the cat that was chasing the mouse."
words = sentence.split()
types = set(words)
token_count = len(words)
type_count = len(types)

print("Type: {} Token: {}".format(type_count, token_count))

hapaxes = [word for word, count in word_counts.items() if count == 1]
print("Hapax Legomenon:", hapaxes)


wordform = ["chases", "chasing"]
lemma = "chase"

# TODO: explore the corpus
#  Go to https://www.english-corpora.org and choose a corpus that seems interesting
#  Think about some phrases you are interested in (very new phrases may not appear)
#  Find five concordances of the words/phrases
text1.concordance('whale')
text1.concordance('ship')

text1.similar('whale')

text1.common_contexts(['ship', 'whale'])




import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import string
import re

# Load the text data
with open('janeeyre.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Preprocess the text
text = text.lower()
text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)  # Remove punctuation
words = text.split()
word_counts = Counter(words)

# TODO: To draw a Zipf's law illustration graph,
#  The x-axis is the rank of the words (1, 2, 3, 4, 5, ...) --> This should be easy
#  The y-axis is the frequency count of each word, from largest to smallest
#  How to get these?
token_count_jane_eyre = len(text)
print("Token Count in 'Jane Eyre' Corpus:", token_count_jane_eyre)

unique_types_jane_eyre = len(set(words))
print("Unique Types Count in 'Jane Eyre' Corpus:", unique_types_jane_eyre)

frequency_whale = text.count('whale')
print("Frequency of 'whale' in 'Jane Eyre' Corpus:", frequency_whale)

normalized_frequency_whale = (frequency_whale / token_count_jane_eyre) * 100
print("Normalized Frequency of 'whale' in 'Jane Eyre' Corpus:", normalized_frequency_whale)

words_gt_10 = [word for word, count in freq_distr_text2.items() if count > 10]
words_gt_10_sorted = dict(sorted(freq_distr_text2.items(), key=lambda item: item[1], reverse=True))
filtered_words = [word for word in freq_distr_text2 if len(word) >= 4 and freq_distr_text2[word] > 10]

words_starting_with_sh = [word for word in freq_distr_text2 if word.startswith('sh')]

print("Words Occurring More Than 10 Times:", words_gt_10)
print("Frequency Dictionary Sorted by Frequency:", words_gt_10_sorted)
print("Filtered Words:", filtered_words)
print("Words Starting with 'sh':", words_starting_with_sh)

ranks = list(range(1, len(frequency) + 1))
#print(ranks)
# Plotting Zipf's Law
plt.figure(figsize=(7, 4))
plt.plot(range(1, len(word_freq) + 1), word_freq, marker='o', linestyle='-', color='b')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.title("Zipf's Law")
plt.grid(True)
plt.show()

# nltk

import nltk
# Download specific resources
nltk.download('webtext')
nltk.download('book')
nltk.download('gutenberg')
nltk.download('nps_chat')
nltk.download('inaugural')
nltk.download('reuters')
nltk.download('udhr')
nltk.download('genesis')

# import all books
from nltk.book import *

# get concordance
# see the context of the word
text1.concordance('whale')
text1.concordance('ship')

# see what words are used in a similar context to a target word
# similar() method identifies words in similar contexts (e.g. syntactic position)
text1.similar('whale')

# the common contexts between two words, num indicates how many contexts to output
text1.common_contexts(['ship', 'whale'], num=50)

# number of tokens in text
len(text1)

# unordered sequence of unique tokens from the text (types)
set(text1)

# number of unique types in a text
len(set(text1))

# count a specific token
text1.count('whale')

# normalized frequency
# the precentage of P(whale)
100 * text1.count('whale')/len(text1)

# list-like operations on nltk objects

# access by index
text1[100]

# slice
text1[100:200]

# get the position of 'whale'
text1.index('whale')

# counting frequency
freq_distr = FreqDist(text1)

# get all the vocabs
vocab = freq_distr.keys()

# get the frequency of specific word
freq_distr['whale']

# get hapaxes
freq_distr.hapaxes()

# get the token with the maximum frequency
freq_distr.max()

# TODO: In text2, find all words that occur more than 10 times;
#  organize the frequency dictionary from largest number to smallest number
#  Get rid of short functions words -- words that have a frequency larger than 10, and the length of word smaller than 4
#  Create a list of words that start with 'sh'
freq_distr_text2 = FreqDist(text2)
# Get words with frequency larger than 10
list_larger_than10 = [w for w in freq_distr_text2.keys() if freq_distr_text2[w] > 10]

# Sort the dictionary from largest to smallest number
dict_sorted = dict(sorted(freq_distr_text2.items(), key = lambda x:x[1], reverse=True))

# Get rid of function words
function_words = [w for w in freq_distr_text2.keys() if freq_distr_text2[w] > 10 and len(w) < 4]

#all_word =
print("Function words:", function_words)
print("Number of function words:", len(function_words))
