import pandas as pd
import string
import os
import sys

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer

import numpy as np
import matplotlib.pyplot as plt

# TODO: Your custom imports here; or copy the functions to here manually.
from evaluation import computeAccuracy, computePrecisionRecall

# TODO: You may need to modify assignment 4 if you just had a main() there.
# my_naive_bayes() should take three arguments: datafile, the review column, and the label column, and return as output 10 floats (numbers)
# representing the metrics.
from Markell2_assignment4 import my_naive_bayes

def main(argv, precision_pos_train=None, recall_pos_train=None, precision_neg_train=None, recall_neg_train=None,
         precision_pos_test=None, recall_pos_test=None, precision_neg_test=None, recall_neg_test=None):
    # argv[1] is the path to 'my_imdb_expanded.csv'
    if len(argv) < 2:
        print("Usage: script.py <my_imdb_expanded.csv>")
        return

    data = pd.read_csv(argv[1], index_col=[0])
    # print(data.head())  # <- Verify the format. Comment this back out once done.
    
    # Part II:
    # Run all models and store the results in variables (dicts).
    # TODO: Make sure you imported your own naive bayes function and it works properly with a named column input!
    # TODO: See also the next todo which gives an example of a convenient output for my_naive_bayes()
    # which you can then easily use to collect different scores.
    # For example (and as illustrated below), the models (nb_original, nb_cleaned, etc.) can be not just lists of scores
    # but dicts where each score will be stored by key, like [TEST][POS][RECALL], etc.
    # But you can also just use lists, except then you must not make a mistake, which score you are accessing,
    # when you plot graphs.
    nb_original = my_naive_bayes(data, 'review', 'label')
    nb_cleaned = my_naive_bayes(data, 'cleaned_review', 'label')
    nb_lowercase = my_naive_bayes(data, 'lowercased', 'label')
    nb_no_stop = my_naive_bayes(data, 'no stopwords', 'label')
    nb_lemmatized = my_naive_bayes(data, 'lemmatized', 'label')

    # Collect accuracies and other scores across models.
    # TODO: Harmonize this with your own naive_bayes() function!
    # The below assumes that naive_bayes() returns a fairly complex dict of scores.
    # (NB: The dicts there contain other dicts!)
    # The return statement for that function looks like this:
    # return({'TRAIN': {'accuracy': accuracy_train, 'POS': {'precision': precision_pos_train, 'recall': recall_pos_train}, 'NEG': {'precision': precision_neg_train, 'recall': recall_neg_train}}, 'TEST': {'accuracy': accuracy_test, 'POS': {'precision': precision_pos_test, 'recall': recall_pos_test}, 'NEG': {'precision': precision_neg_test, 'recall': recall_neg_test}}})
    # This of course assumes that variables like "accuracy_train", etc., were assigned the right values already.
    # You don't have to do it this way; we are giving it to you just as an example.
    train_accuracies = []
    test_accuracies = []
    
    precision_pos_train = []
    recall_pos_train = []
    precision_neg_train = []
    recall_neg_train = []
    precision_pos_test = []
    recall_pos_test = []
    precision_neg_test = []
    recall_neg_test = []
    # TODO: Initialize other score lists similarly. The precision and recalls, for negative and positive, train and test.
    for model in [nb_original, nb_cleaned, nb_lowercase, nb_no_stop, nb_lemmatized]:
        # TODO: See comment above about where this "model" dict comes from.
        # If you are doing something different, e.g. just a list of scores,
        # that's fine, change the below as appropriate,
        # just make sure you don't confuse where which score is.
        train_accuracies.append(model['TRAIN']['accuracy'])
        test_accuracies.append(model['TEST']['accuracy'])
        # TODO: Collect other scores similarly. The precision and recalls, for negative and positive, train and test.
        precision_pos_train.append(model['TRAIN']['POS']['precision'])
        recall_pos_train.append(model['TRAIN']['POS']['recall'])
        precision_neg_train.append(model['TRAIN']['NEG']['precision'])
        recall_neg_train.append(model['TRAIN']['NEG']['recall'])
        precision_pos_test.append(model['TEST']['POS']['precision'])
        recall_pos_test.append(model['TEST']['POS']['recall'])
        precision_neg_test.append(model['TEST']['NEG']['precision'])
        recall_neg_test.append(model['TEST']['NEG']['recall'])
    # TODO: Create the plot(s) that you want for the report using matplotlib (plt).
    # Use the below to save pictures as files:
    # plt.savefig('filename.png')
    # If you stored the plot into a variable, the line for saving picture will be
    # plotname.savefig('filename.png')
    plt.figure(figsize=(10, 6))
    plt.plot(train_accuracies, label='Train Accuracy')
    plt.plot(test_accuracies, label='Test Accuracy', linestyle='dotted')
  
    plt.plot(precision_pos_train, label='precision pos train')
    plt.plot(precision_pos_test, label='Precision pos test', linestyle='dotted')
  
    plt.plot(precision_neg_train, label='Precision neg train')
    plt.plot(precision_neg_test, label='Precision neg test', linestyle='dotted')
  
    plt.xlabel('Model Variants')
    plt.ylabel('Accuracy')
    plt.title('Accuracies, Positive and Negative Precision of Different Models')
    plt.legend()
    plt.savefig('Graph1.png')

    plt.clf()
    plt.figure(figsize=(10, 6))
    plt.plot(recall_pos_train, label='recall pos train')
    plt.plot(recall_pos_test, label='recall pos test', linestyle='dotted')
  
    plt.plot(recall_neg_train, label='recall neg train')
    plt.plot(recall_neg_test, label='recall neg test', linestyle='dotted')
  
    plt.xlabel('Model Variants')
    plt.ylabel('Accuracy')
    plt.title('Positive and Negative recall of Different Models')
    plt.legend()
    plt.savefig('Graph2.png')


if __name__ == "__main__":
    main(sys.argv)
