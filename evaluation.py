
'''
Recommended zip() function and list comprehension to implement.
You can do things differently if you like, so long as you get correct results.

The function takes two lists (arrays), one of system predictions and one of gold labels.
The assumption is that the lists are of equal length and the order of elements in both lists
corresponds to the order of data points in the dataset. It is the responsibility of 
the function caller to ensure that is the case; otherwise the function won't return
anything meaningful.

The function computes the accuracy by comparing the predicted labels to gold labels.
Accuracy = correct predictions / total predictions
Consider also recording the indices of the data points for which a wrong prediction was made.
The function can then return a tuple: (accuracy, mistakes) where accuracy is a float
and mistakes is a list of integers.
'''


def computeAccuracy(predictions, gold_labels):
    # The assert statement will notify you if the condition does not hold.
    assert len(predictions) == len(gold_labels)
    accuracy = None
    mistakes = []  # Consider keeping a record of the indices of the errors.
    return (accuracy, mistakes)


'''
Recommand zip() function and list comprehension to implement
You can do things differently if you like (including changing what is passed in), 
so long as you get correct results.

As suggested, the function takes three arguments. 
The first two are arrays (lists), one of predicted labels and one of actual (gold) labels.
The third argument is a string indicating which class the precision is computed for.
This is the confusing part! You can compute precision and recall wrt the positive reviews 
or wrt the negative reviews! What is considered a "true positive" depends on what the relevant class is!

The function then computes precision as per definition: true positives / (true positives + false positives)
And it computes recall as per definition: true positives / (true positives + false negatives)

This fucntion returns a tuple of floats: (precision, recall)
'''


def computePrecisionRecall(predictions, gold_labels, relevant_class):
    assert len(predictions) == len(gold_labels)
    if relevant_class == "POSITIVE":
        opposite_class = "NEGATIVE"
    else:
        opposite_class = "POSITIVE"
    #true positive

    #true negative

    #false positive

    #false negative

    precision = None
    recall = None

    return None
