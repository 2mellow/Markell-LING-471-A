# Adapted from Matthew C. Kelley, 2022
# Updated by Yuan Chai, 2024

import sys
import pandas as pd

import sys
import pandas as pd
from collections import Counter

# This convert_to_wordlist() function will take a column in the datafile,
# and convert it into a list with each individual word as an item
def convert_to_wordlist(column):
    text = column.str.cat()
    wordlist = text.split()
    return wordlist



def largest_counts(data):
    # TODO: Cut up the rows in the dataset according to how you stored things.
    # The below assumes your data has a column of "type", storing whether the review is pos or neg
    # If you did differently, make corresponding changes
    print(data[(data['type'] == "test")])
    pos_data = data[(data['type'] == "train") & (data['label'] == 1)]
    neg_data = data[(data['type'] == "train") & (data['label'] == 0)]

    data_cut = [pos_data, neg_data]
    # by value (count) in reverse (descending) order.
    # It is your task to Google and learn how to do this, but we will help of course,
    # if you come to use with questions. This can be daunting at first, but give it time.
    # Spend some (reasonable) time across a few days if necessary, and you will do it!
    model = ["review", "cleaned_review", "no stopwords", "lemmatized"]

    # Loop over the four portions of data, and loop over each model
    # Create a counting dictionary for each one
    # Store the 20 most frequent words into count.txt file
    for dataindex, dataitem in enumerate(data_cut):
        datafile_name = [name for name, value in locals().items() if value is dataitem][0]
        for modelindex, modelitem in enumerate(model):
            wordlist = convert_to_wordlist(dataitem[modelitem])
            freq_dict = Counter(wordlist)
            # TODO: SORT the count dictionary in the preceding line in a descending order
            #  Google learn how to do this; this has also been covered on the class of 05/21/24
            freq_dict_sort = dict(sorted(freq_dict.items(), key=lambda item: item[1], reverse=True))

            # Write the most frequent 20 words into a txt file
            if dataindex ==0 and modelindex == 0:
                with open('counts.txt', 'w', encoding="utf-8") as f:
                    f.write(datafile_name + '\t' + modelitem + ':\n')
                    for k, v in list(freq_dict_sort.items())[:20]:
                        f.write('{}\t{}\n'.format(k, v))
                    f.write('\n')
            else:
                with open('counts.txt', 'a', encoding="utf-8") as f:
                    f.write(datafile_name+'\t'+modelitem+':\n')
                    for k, v in list(freq_dict_sort.items())[:20]:
                        f.write('{}\t{}\n'.format(k, v))
                    f.write('\n')



def main(argv):
    data = pd.read_csv(argv[1], index_col=[0])
    
    train_data = data[data['type']=='train']
    # print(train_data.head())  # <- Verify the format. Comment this back out once done.
    
    largest_counts(train_data)


if __name__ == "__main__":
    main(sys.argv)
