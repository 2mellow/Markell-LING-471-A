__author__ = 'Markell Thornton'

import sys
from pathlib import Path
from collections import Counter
# OK, we have successfully read the files.
# Now we need to convert the long text files into each individual sentence.
# And we need to store the word and its corresponding tags within each sentences.

# Our training data looks like this:
'''
i	PRP
'd	MD
like	VB
french	JJ
food	NN
.	.

next	JJ
thursday	NN
.	.

next	JJ
thursday	NN
.	.

dinner	NN
.	.

i	PRP
want	VBP
to	TO
have	VB
dinner	NN
.	.

'''


# We want it to look like this:

# list_observe_tag = [("<s>","start"),("I","PRP"), ("want","VBP), ("to","TO"), ("have","VB"), ("dinner","NN"), (".",".")]
# list_observe = ["<s>","I","want","to","have","dinner","."]
# list_tag = ["start","PRP","VBP","TO","VB","NN","."]


def reformat(file):
    # step 1: arrange the input file into lists
    # observe_tag is list consist of tuples (observation, tag);
    # list_observe consists of observations
    # list_tag consists of tags
    # Those three lists are aligned in the same order
    # global vocab, dict_observe_count, dict_tag_count, bigram_tag_count, dict_observe_prob, dict_tran_prob, list_tag_unique
    # read each line in the file

    # Note that we have ("<s>","start") at the beginning of each sentence.
    # That means we need to know the boundary of each sentence.
    # The first task would be reformat the file into a list of lists. Each nested list consists of a sentece.

    with open(file, 'r', encoding='utf-8') as text:
        # read the file by line
        list_read_text = [line.strip() for line in text]
    # print(list_read_text[:20])
    # remove empty items in the lines
    list_line = [line for line in list_read_text if line != ""]
    # print(list_line[:20])

    # TODO: find a way to insert a '<s>\tstart' at the beginning of each sentence
    # Create a list_observe_tag, storing each word and tag as a tuple in a list
    # The first five output should look likt this:
    list_observe_tag = []
    sentence_start = True
    
    for index, item in enumerate(list_line):
        if item == ".\t.":
            list_line.insert(index + 1, "<s>\tstart")
        elif index == 0:
            list_line.insert(0, "<s>\tstart")
            entence_start = False
        word, tag = item.split("\t")
        list_observe_tag.append((word, tag))
        if word == "." and tag == ".":
            sentence_start = True

    list_observe = [x for (x, y) in list_observe_tag]
    list_tag = [y for (x, y) in list_observe_tag]
            
    for item in list_line:
        list_observe_tag.append(tuple(item.split("\t")))

    list_observe = [x for (x, y) in list_observe_tag]
    list_tag = [y for (x, y) in list_observe_tag]
    # print(list_observe_tag[:20])
    # print(list_observe[:20])
    # print(list_tag[:20])

    return list_observe_tag, list_observe, list_tag


# In order to calculate conditional probability P(word|tag),
# P(word|tag) = P(word & tag) / P(tag)
# So we need to get a count of each pair of word and tag, divided by all combinations of word and tag
# P(tag) would just be the count of the specific tag divided by the count of all tags
# We also need P(tag1|tag2)
# P(tag1|tag2) = P(tag1 tag2) / P(tag2)
# So we need to get a count of all combinations of tag, divided by the count of the second tag


def prob(list_observe_tag, list_observe, list_tag):
    # TODO: Return two lists, dict_observe_prob and dict_tran_prob
    # dict_observe_prob stores the probability of each word given its tag
    # the first three elements in dict_observe_prob are:
    # dict_observe_prob = {{('<s>', 'start'): 1.0, ('i', 'PRP'): 0.610793775851881, ("'d", 'MD'): 0.2630635245901639}

    # dict_tran_prob stores the probability of each tag given the previous tag:
    # the first three elements in dict_tran_prob are:
    # dict_tran_prob = {('start', 'PRP'): 0.34782262558713384, ('PRP', 'MD'): 0.2762458144573558, ('MD', 'VB'): 0.799436475409829}

    # this gives a count of each (word, tag) tuple
    dict_observe_count = dict(Counter(list_observe_tag).items())
    from itertools import islice
    dict_observe_count = dict(Counter(list_observe_tag).items())
    dict_tag_count = dict(Counter(list_tag).items())
    list_tag_unique = list(dict_tag_count.keys())
    
    # print(dict(islice(dict_observe_count.items(), 0, 20)))

    # TODO: Get a count of the tags in the list_tag
    # The output should look like:
    # {'start': 12561, 'PRP': 10154, 'MD': 3904, 'VB': 11595, 'JJ': 6187, ...}
    dict_observe_prob = {
        item: observe_count / dict_tag_count[item[1]]
        for item, observe_count in dict_observe_count.items()
    }
    
    # dict_tag_count: the frequency of each tag
    dict_tag_count = dict(Counter(list_tag).items())

    # print(dict(islice(dict_tag_count.items(), 0, 20)))

    # TODO: Store the unique lists in list_tag_unique. You don't need it for today. But it will be helpful tomorrow.
    # list_tag_unique stores the key of the dict. The tag order is the same as the keys in list_tag_count
    # It looks like: ['start', 'PRP', 'MD', 'VB', 'JJ', 'NN', '.', 'VBP', 'TO', 'RB', 'IN', 'FW', 'DT', 'HYPH', 'RP', 'WDT', 'NNS', 'CD', 'VBD', 'UH', 'JJR', 'NNP', 'POS', 'CC', 'WRB', 'VBZ', 'WP', 'PRP$', 'VBG', 'JJS', 'EX', 'VBN', 'RBR', 'RBS', 'PDT', ':']
    list_tag_unique = list(dict_tag_count.keys())
    # print(list_tag_unique)

    # Step 1: calculate observation probablity P(word|tag) = P(tag&word) / P(tag)
    dict_observe_prob = {}
    for item in dict_observe_count:
        # item is a tuple: ("eleven", CD)
        # tag is the POS tag of each tuple
        tag = item[1]
        # observe_count get the count of the word & tag in the dict
        observe_count = dict_observe_count[item]
        # tag_count get the count of the tag from dict_tag_count
        tag_count = dict_tag_count[tag]
        # P(word|tag) = P(word & tag) / P(tag)
        # P(word & tag) = the count of (word & tag) / the total number of (word & tag) in corpus
        # P(tag) = the count of (tag) / the total number of tags in the corpus
        # The denominator number is the same --> how many words there are in the corpus
        # So no need to include the denominator
        dict_observe_prob[item] = observe_count / tag_count

    # Step 2: calculate transitional probablity P(tag1|tag2) for every possible combinations of two tags
    # first, create a list of every two consecutive tags
    list_bigram_tag = [item for item in zip(list_tag, list_tag[1:])]
    # print(list_bigram_tag[:20])
    # then, count the occurance of each tag sequence
    bigram_tag_count = dict(Counter(list_bigram_tag).items())
    # print(dict(islice(bigram_tag_count.items(), 0, 20)))

    # dict_tran_prob: store the transitional probability
    vocab = len(dict_tag_count)
    dict_tran_prob = {}
    for bigram_tag in bigram_tag_count:
        # bigram_tag: the bigram tag the prob is being calculated
        cnt_bigram_tag = bigram_tag_count[bigram_tag]
        # tag_i_1: the first tag in the bigram tag tuple
        tag_i_1 = bigram_tag[0]
        # get the count of the t-1 tag from the list_tag count
        cnt_tag_i_1 = dict_tag_count[tag_i_1]
        # the probablity of the bigram tag sequence is the count of the bigram over the count of tag i-1
        # do plus small number smoothing P(tag2|tag1) = P(tag1 tag2) / P(tag1)
        bigram_tag_prob = (cnt_bigram_tag + 0.000000000001) / (cnt_tag_i_1 + vocab * 0.000000000001)
        dict_tran_prob[bigram_tag] = bigram_tag_prob
    # make the probability of start and end transitions as 0
    dict_tran_prob.update({("start", "start"): 0, ("start", "."): 0, (".", "start"): 0, (".", "."): 0})
    # print(dict(islice(dict_observe_prob.items(), 0, 20))) #P(word|tag)
    # print(dict(islice(dict_tran_prob.items(), 0, 20))) #P(tag2|tag1)
    return dict_observe_prob, dict_tran_prob, list_tag_unique, dict_tag_count


def reformatWordlist(file):
    with open(file, 'r', encoding='utf-8') as text:
        # read the file by line
        list_read_text = [line.strip() for line in text]
    list_line = [line for line in list_read_text if line != ""]

    current_sentence = []
    list_sentence = []
    for word in list_line:
        current_sentence.append(word)
        if word == '.':
            list_sentence.append(current_sentence)
            current_sentence = []

    return list_line, list_sentence
