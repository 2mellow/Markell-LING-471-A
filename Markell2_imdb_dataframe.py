# Skeleton for Assignment 4, Part 1
# Created by Olga Zamaraeva for Ling471, Spring 2021
# Updated by Matthew C. Kelley for Ling 471, Spring 2023
# Updated by Yuan Chai for Ling 471, Spring 2024

import sys
import re
import string
from pathlib import Path

import pandas as pd


'''
The function below should be called on a file name.
It is the cleanFileContents() function that we have used for Assignments 2 and 3.

If you don't want to copy and paste the function below,
you can use 
from assignment2 import cleanFileContents() (substitute assignment 2 with your own assignment2 filename)
to make your codes neater.

cleanFileContents() function opens the file, reads its contents, and stores it in a variable.
Then, it removes punctuation marks, and returns the "cleaned" text.
'''


def cleanFileContents(f):
    with open(f, 'r', encoding='utf-8') as f:
        text = f.read()
    clean_text = text.translate(str.maketrans('', '', string.punctuation))
    clean_text = re.sub(r'\s+', ' ', clean_text)
    return clean_text



'''
Write a function which accepts a list of 4 directories:
train/pos, train/neg, test/pos, and test/neg.

The result of calling this program on the 4 directories is a new .csv file in the working directory.
'''

# Constants:
POS = 1
NEG = 0


def createDataFrame(argv, label, data_type):
    # TODO: Create a single dataframe from the 4 IMBD directories (passed as argv[1]--argv[4]).
    # For example, "data" can be a LIST OF LISTS.
    # In this case, each list is a set of column values, e.g. ["0_2.txt", "neg", "test", "Once again Mr Costner..."].
    # That is, each list represents a single row in your data frame.
    # You may use a different way of creating a dataframe so long as the result is accurate.
    # TODO: Call the cleanFileContents() function on each file, as you are iterating over them.
    data = []
    # Your code here...
    path = Path(argv)
    for file_path in path.glob('*.txt'):
        cleaned_text = cleanFileContents(file_path)
        data.append([file_path.name, label, data_type, cleaned_text])
    return data

    # Try to create a list of lists, for example, as illustrated above.
    # Consider writing a separate function which takes a filename and returns a list representing the reivew vector.
    # This will make your code here cleaner.
    # HINT: You when you are trying to get the pos/neg value and the test/train value,
    # you may want to use the `parts` attribute of a `Path` object; try yourpathvariable.parts and see what the output values are.


    # Once you are done, the code below will only require modifications if your data variable is not a list of lists.
    # Sample column names; you can use different ones if you prefer,
    # but then make sure to make appropriate changes in assignment4_skeleton.py.



def main(argv):
    # Process each directory and collect the data
    train_pos_data = createDataFrame(argv[1], POS, "train")
    train_neg_data = createDataFrame(argv[2], NEG, "train")
    test_pos_data = createDataFrame(argv[3], POS, "test")
    test_neg_data = createDataFrame(argv[4], NEG, "test")

    data = test_pos_data + test_neg_data + train_pos_data + train_neg_data

    column_names = ["file", "label", "type", "review"]
    # Sample way of creating a dataframe. This assumes that "data" is a LIST OF LISTS.
    df = pd.DataFrame(data=data, columns=column_names)
    # Saving to a file:
    new_filename = "my_imdb_dataframe.csv"
    df.to_csv(new_filename)

if __name__ == "__main__":
    main(sys.argv)
