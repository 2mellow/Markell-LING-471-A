# Olga Zamaraeva's solution for Assignment 3 from Ling471 Spring 2021.
# Copyright Olga Zamaraeva, 2021
# Updated by Matthew C. Kelley, 2022
# Updated by Yuan Chai, 2024

import sys
import re
import string
from pathlib import Path

import pandas as pd
import csv

from bs4 import BeautifulSoup
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk import stem
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

# Constants:
POS = 1
NEG = 0


def review_to_words(review, remove_stopwords=False, lemmatize=False):
    # Getting an off-the-shelf list of English "stopwords"
    stops = stopwords.words('english')
    # Initializing an instance of the NLTK stemmer/lemmatizer class
    sno = stem.SnowballStemmer('english')
    # Removing HTML using BeautifulSoup preprocessing package
    review_text = BeautifulSoup(review, "html.parser").get_text()
    # Remove non-letters using a regular expression
    review_text = re.sub("[^a-zA-Z]", " ", review_text)
    # Tokenizing by whitespace
    words = review_text.split()
    # Recall "list comprehension" from the lecture demo and try to understand what the below loops are doing:
    if remove_stopwords:
        words = [w for w in words if not w in stops]
    if lemmatize:
        lemmas = [sno.stem(w).encode('utf8') for w in words]
        # The join() function is a built-in method of strings.
        # The below says: iterate over the "lemmas" list and create
        # a new string where each item in "lemmas" is added to this new string,
        # and the items are separated by a space.
        # The b-thing is a quirk of the SnowballStemmer package.
        return b" ".join(lemmas)
    else:
        return ' '.join(words)


def cleanFileContents(f):
    with open(f, 'r', encoding='utf-8') as f:
        text = f.read()
    cleaned_text = review_to_words(text)
    lowercased = cleaned_text.lower()
    no_stop = review_to_words(lowercased, remove_stopwords=True)
    lemmatized = review_to_words(no_stop, lemmatize=True)
    return (text, cleaned_text, lowercased, no_stop, lemmatized)


def processFileForDF(f, table, label, type):
    text, cleaned_text, lowercased, no_stop, lemmatized = cleanFileContents(f)
    table.append([f.stem+'.txt', label, type, text,
                 cleaned_text, lowercased, no_stop, lemmatized])


def createDataFrames(argv):
    train_pos = list(Path(argv[1]).glob("*.txt"))
    train_neg = list(Path(argv[2]).glob("*.txt"))
    test_pos = list(Path(argv[3]).glob("*.txt"))
    test_neg = list(Path(argv[4]).glob("*.txt"))

    data = []

    # TODO: Your function from assignment 4, adapted for assignment 5 as needed, goes here.
    # Do all the required preprocerssing.
    # You can use the processFileForDF() function to store each row of the data.
    # TODO: The program will now be noticeably slower!
    # To reassure yourself that the program is doing something, insert print statements as progress indicators.
    # For example, for each 100th file, print out something like:
    # "Processing directory 1 out of 4; file 99 out of 12500".
    # The enumerate method iterates over both the items in the list and their indices, at the same time.
    # Step through in the debugger to see what i and f are at step 1, step 2, and so forth.

    # Your code goes here... Example of how to get not only a list element but also its index, below:
    # for index, element in enumerate(['a','b','c','d']):
    #    print("{}'s index is {}".format(element,index))
    # Processing training positive files
    num_dirs = 4

    # Processing training positive files
    for i, f in enumerate(train_pos):
        dir_num = (i // (len(train_pos) // num_dirs)) + 1
        if i % 100 == 0:
            print(f"Train POS: Processing dir {dir_num}/{num_dirs}, file {i + 1} out of {len(train_pos)}")
        processFileForDF(f, data, POS, 'train')

    # Processing training negative files
    for i, f in enumerate(train_neg):
        dir_num = (i // (len(train_neg) // num_dirs)) + 1
        if i % 100 == 0:
            print(f"Train NEG: Processing dir {dir_num}/{num_dirs}, file {i + 1} out of {len(train_neg)}")
        processFileForDF(f, data, NEG, 'train')

    # Processing testing positive files
    for i, f in enumerate(test_pos):
        dir_num = (i // (len(test_pos) // num_dirs)) + 1
        if i % 100 == 0:
            print(f"Test POS: Processing dir {dir_num}/{num_dirs}, file {i + 1} out of {len(test_pos)}")
        processFileForDF(f, data, POS, 'test')

    # Processing testing negative files
    for i, f in enumerate(test_neg):
        dir_num = (i // (len(test_neg) // num_dirs)) + 1
        if i % 100 == 0:
            print(f"Test NEG: Processing dir {dir_num}/{num_dirs}, file {i + 1} out of {len(test_neg)}")
        processFileForDF(f, data, NEG, 'test')

    # Use the below column names if you like:
    column_names = ["file", "label", "type", "review",
                    "cleaned_review", "lowercased", "no stopwords", "lemmatized"]

    df = pd.DataFrame(data=data, columns=column_names)
    #df.sort_values(by=['type', 'file'])
    df.to_csv('my_imdb_expanded.csv')


def main(argv):
    createDataFrames(argv)


if __name__ == "__main__":
    main(sys.argv)