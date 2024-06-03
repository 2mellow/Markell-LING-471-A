# Skeleton for Assignment 4, Part 2
# Created by Olga Zamaraeva for Ling471, Spring 2021
# Updated by Matthew C. Kelley for Ling 471, Spring 2023
# Updated by Yuan Chai for Ling 471, Spring 2024


import pandas as pd
import string
import sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# These are your own functions you wrote for Assignment 3:
from evaluation import computePrecisionRecall, computeAccuracy
# Note: If you did not put your functions into the `evaluation.py` file
# import the functions however you need, or copy and paste them into this file
# (and you would then need  to delete the `from evaluation import...` line above)

# Constants
ROUND = 4
GOOD_REVIEW = 1
BAD_REVIEW = 0
ALPHA = 1


def my_naive_bayes(datafile:str, review_col:str,label_col:str):
    
    # Read in the data. NB: You may get an extra Unnamed column with indices; this is OK.
    # If you like, you can get rid of it by passing a second argument to the read_csv(): index_col=[0].
    data = datafile
  
    
    # TODO: Change as appropriate, if you stored data differently (e.g. if you put train data first).
    # You may also make use of the "type" column here instead! E.g. you could sort data by "type".
    # At any rate, make sure you are grabbing the right data! Double check with temporary print statements,
    # e.g. print(test_data.head()).
    
    total_count = data.shape[0]
    
    test_data = data[:25000]  # Assuming the first 25,000 rows are test data.

    # Assuming the second 25,000 rows are training data. Double check!
    train_data = data[25000:50000]

    # TODO: Set the below 4 variables to contain:
    # X_train: the training data; y_train: the training data labels;
    # X_test: the test data; y_test: the test data labels.
    # Access the data frames by the appropriate column names.
    # Hint: df['column name']
    X_train = train_data[review_col]
    y_train = train_data[label_col]
    X_test = test_data[review_col]
    y_test = test_data[label_col]
    
    # The next three lines are performing feature extraction and word counting. 
    # They are choosing which words to count frequencies for, basically, to discard some of the noise.
    # If you are curious, you could read about TF-IDF,
    # e.g. here: https://www.geeksforgeeks.org/tf-idf-model-for-page-ranking/
    # or here: https://en.wikipedia.org/wiki/Tf%E2%80%93idf
    # TODO: Add a general brief comment on why choosing which words to count may be important.
    tf_idf_vect = TfidfVectorizer(ngram_range=(1, 2))
    tf_idf_train = tf_idf_vect.fit_transform(X_train.values)
    tf_idf_test = tf_idf_vect.transform(X_test.values)

    ### Because choosing the right words can increase the accuracy of preditions.
    ### It'll exclude language that doesn't matter and better than doing == [Word, In, List]

    # TODO COMMENT: The hyperparameter alpha is used for Laplace Smoothing.
    # Add a brief comment, trying to explain, in your own words, what smoothing is for.
    # You may want to read about Laplace smoothing here: https://towardsdatascience.com/laplace-smoothing-in-na%C3%AFve-bayes-algorithm-9c237a8bdece
    clf = MultinomialNB(alpha=ALPHA)

    ### Laplace Smoothing is used in probability
    ### when there are zero probabilities and used to improve the accuracy of models.

    # TODO COMMENT: Add a comment explaining in your own words what the "fit()" method is doing.
    clf.fit(tf_idf_train, y_train)

    ### The fit() function takes in two parameters and allows the model to learn and understand patterns.

    # TODO COMMENT: Add a comment explaining in your own words what the "predict()" method is doing in the next two lines.
    y_pred_train = clf.predict(tf_idf_train)
    y_pred_test = clf.predict(tf_idf_test)

    ### Predict function in the 1st line check how much the model learned from the data used in training
    ### The second predict checks performance of the model on new data, by trying to predict their labels.

    # TODO: Compute accuracy, precision, and recall, for both train and test data.
    # Import and call your methods from evaluation.py (or wherever) which you wrote for HW3.
    # Note: If you methods there accept lists, you will probably need to cast your pandas label objects to simple python lists:
    # e.g. list(y_train) -- when passing them to your accuracy and precision and recall functions.

    accuracy_test = computeAccuracy(list(y_test), list(y_pred_test))[0]
    accuracy_train = computeAccuracy(list(y_train), list(y_pred_train))[0]
    
    # Compute precision and recall for positive class on test dataset
    precision_pos_test, recall_pos_test = computePrecisionRecall(list(y_pred_test), list(y_test), GOOD_REVIEW)
    # Compute precision and recall for negative class on test dataset
    precision_neg_test, recall_neg_test = computePrecisionRecall(list(y_pred_test), list(y_test), BAD_REVIEW)

    # Compute precision and recall for positive class on train dataset
    precision_pos_train, recall_pos_train = computePrecisionRecall(list(y_pred_train), list(y_train), GOOD_REVIEW)
    # Compute precision and recall for negative class on train dataset
    precision_neg_train, recall_neg_train = computePrecisionRecall(list(y_pred_train), list(y_train), BAD_REVIEW)

    return {
        "TRAIN": {
            'accuracy': accuracy_train,
            'POS': {
                'precision': precision_pos_train,
                'recall': recall_pos_train,
            },
            'NEG': {
                'precision': precision_neg_train,
                'recall': recall_neg_train,
            }
        },
        "TEST": {
            'accuracy': accuracy_test,
            'POS': {
                'precision': precision_pos_test,
                'recall': recall_pos_test,
            },
            'NEG': {
                'precision': precision_neg_test,
                'recall': recall_neg_test,
            }
        }
    }
    


# This function will be reporting errors due to variables which were not assigned any value.
# Your task is to get it working! You can comment out things which aren't working at first.
def main(argv):
    data = pd.read_csv(argv[1])
    model = my_naive_bayes(data, 'text','label')
    
    accuracy_test = model['TEST']['accuracy']
    accuracy_train = model['TRAIN']['accuracy']
    
    precision_pos_test, recall_pos_test = model['TEST']['POS']['precision'],model['TEST']['POS']['recall'] 
    precision_neg_test, recall_neg_test =  model['TEST']['NEG']['precision'],model['TEST']['NEG']['recall'] 

    precision_pos_train, recall_pos_train =  model['TRAIN']['POS']['precision'],model['TRAIN']['POS']['recall'] 
    precision_neg_train, recall_neg_train = model['TRAIN']['POS']['precision'],model['TRAIN']['POS']['recall'] 

    print("Train accuracy:           \t{}".format(round(accuracy_train, ROUND)))
    print("Train precision positive: \t{}".format(
        round(precision_pos_train, ROUND)))
    print("Train recall positive:    \t{}".format(
        round(recall_pos_train, ROUND)))
    print("Train precision negative: \t{}".format(
        round(precision_neg_train, ROUND)))
    print("Train recall negative:    \t{}".format(
        round(recall_neg_train, ROUND)))
    print("Test accuracy:            \t{}".format(round(accuracy_test, ROUND)))
    print("Test precision positive:  \t{}".format(
        round(precision_pos_test, ROUND)))
    print("Test recall positive:     \t{}".format(
        round(recall_pos_test, ROUND)))
    print("Test precision negative:  \t{}".format(
        round(precision_neg_test, ROUND)))
    print("Test recall negative:     \t{}".format(
        round(recall_neg_test, ROUND)))


if __name__ == "__main__":
    main(sys.argv)
