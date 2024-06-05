# Let's do a POS tagging task together
# Step 1: import the text

import sys
from pathlib import Path
from collections import Counter
from train import reformat, reformatWordlist, prob

f_train = Path("train.txt")
f_test = Path("test.txt")

# TODO: First, fill in all the TODO codes underneath
# TODO: Upload your output_test.txt canvas. It would contain all the words in test.txt and the corresponding tags
# TODO: Use the rest of the time to understand this script, and improve this script
#  The part needs most impovement is in viterbi_recursion()
# TODO: Use the rest of the time to calculate the accuracy, precision, and recall for each POS tagging by comparing your output_test.txt with the test_goldstandard.txt
# For example, PP: accuracy, precision, recall; NN: accuracy, precision, recall; VB: accuracy, precision, recall
#  The first 26 lines look like this:
'''
i	PRP
'd	MD
like	VB
to	TO
go	VB
to	IN
a	DT
fancy	JJ
restaurant	NN
.	.

i	PRP
want	VBP
to	TO
eat	VB
french	JJ
food	NN
.	.

i	PRP
want	VBP
to	TO
eat	VB
breakfast	NN
instead	RB
.	.
'''
alpha = 0.000000000001

# print(test[:20])

# Here comes viterbi

# viterbi_initial returns a list of P(tag|start) * P(first word)
# The output of viterbi_initial stores a probability for each tag
def viterbi_initial(sentence, dict_observe_prob, dict_tran_prob, list_tag_unique, dict_tag_count):
    global vocab
    vocab = len(dict_tag_count)
    # print(list_sentence[:5])
    list_v1 = []

    # initialization; from start to the next tag
    for tag in list_tag_unique:
        if ("start", tag) in dict_tran_prob:
            # TODO: if you can find the transition of ("start", tag), what should the tran_prob be for your test data?
            tran_prob = dict_tran_prob[("start", tag)]
        else:
            # TODO: if you cannot find the transition of ("start", tag), you are going to do smoothing by assigning a very small number to it.
            # smoothing formula is alpha/tag1 + vocab * alpha
            tran_prob = alpha / (dict_tag_count["start"] + vocab * alpha)

        if (sentence[0], tag) in dict_observe_prob:
            # TODO: if you can find the word|tag key in the dict_observe_prob, what will you assign to the obser_prob?
            observe_prob = dict_observe_prob[(sentence[0], tag)]
        else:
            observe_prob = alpha
        v1 = tran_prob * observe_prob
        # store the value in list_v1. Now in list_v1, you get the probability of
        # the transition probability of start to all the possible tags
        # multiply the probability of the first word given each possible tag
        list_v1.append(v1)
    # append the list of from start to first stage viterbi result into the list of viterbi of all stages
    return list_v1

def viterbi_recursion(sentence, dict_observe_prob, dict_tran_prob, list_tag_unique, dict_tag_count, list_v1):
    # store the back tracing
    list_v = [list_v1]
    list_back = []
    # recursion

    # not counting for the first word "<s>" and the last word "."
    for index in range(len(sentence) - 2):
        list_recursion = []
        list_recursion_back = []
        list_tag_name = []
        list_tag_name_recursion = []
        observe = sentence[1:][index]
        for tag in list_tag_unique:
            # list_each consists of the v from state i at time j-1
            list_each = []
            # list_each_back consists of the backpointer from time j to time j-1
            # list_each and list_each_back are parallel
            list_each_back = []

            if (observe, tag) in dict_observe_prob:
                observe_prob = dict_observe_prob[(observe,tag)]
            else:
                observe_prob = 0.000000000001

            # tag_i_1 is the tag from the previous stage. We have to get the v, the transition, and the observation probability for each tag
            for tag_i_1 in list_tag_unique:
                # back_each is the index of the previous tag under calculation
                back_each = list_tag_unique.index(tag_i_1)
                # store the back tag index into a list
                list_each_back.append(back_each)
                # calculate the transitional probability from the previous tag to the current tag
                if (tag_i_1, tag) in dict_tran_prob:
                    # TODO: if (tag_i_1) and the current tag is in dict_tran_prob, what should you assign to dict_tran_prob?
                    tran_prob = dict_tran_prob[(tag_i_1, tag)]
                else:
                    # TODO: if (tag_i_1) and the current tag is in dict_tran_prob, what should you assign to dict_tran_prob?
                    # formula: alpha / alpha + vocab size * alpha
                    tran_prob = alpha / (dict_tag_count[tag_i_1] + vocab * alpha)
                    
                    # v of every path to one tag
                # list_v[index]: which word we are at right now.
                # list_v[index][back_each]: the v of which tag
                vi = observe_prob * tran_prob * list_v[index][back_each]
                # the probability of the current stage
                list_each.append(vi)
            # the max v to that tag
            vi_max = max(list_each)
            # vi_back stores where that max v comes from
            vi_back = list_each_back[list_each.index(vi_max)]
            # store the maximum probability value to the back pointer
            list_recursion.append(vi_max)
            # store the tag into list_recursion_back
            list_recursion_back.append(vi_back)

        # the v of each state at the observation time
        list_v.append(list_recursion)
        list_back.append(list_recursion_back)
        list_tag_name.append(list_tag_name_recursion)
    return list_v, list_back, list_tag_name

def viterbi_end(sentence, dict_tran_prob, list_tag_unique, dict_tag_count, list_v,list_back):
    # end
    list_end = []
    for tag in list_tag_unique:
        if (tag, ".") in dict_tran_prob:
            # TODO: if (tag, ".") is in dict_tran_prob, what should you assign to dict_tran_prob?
            tran_prob = dict_tran_prob[(tag, ".")]
        else:
            # TODO: if (tag, ".") is not in dict_tran_prob, what should you assign to dict_tran_prob?
            # formula: alpha / count of tag1 + vocab * alpha
            tran_prob = alpha / (dict_tag_count[tag] + vocab * alpha)

        v_end = tran_prob * list_v[-1][list_tag_unique.index(tag)]
        list_end.append(v_end)

    v_final = max(list_end)
    pre_state = list_end.index(v_final)

    # the state at the observation time prior to end time
    list_trace = []
    list_trace.append(pre_state)
    # list_sequence stores the state of each observation time
    list_sequence = []
    # TODO: look for what [::-1] does and leave a comment
    list_range = list(range(len(list_back)))[::-1]
    list_sequence.append(list_tag_unique[pre_state])
    for index in list_range:
        pre = list_back[index][list_trace[list_range.index(index)]]
        list_trace.append(pre)
        list_sequence.insert(0, list_tag_unique[pre])

    for index in range(len(list_sequence)):
        list_sequence[index] = sentence[index] + "\t" + list_sequence[index] + '\n'
    list_sequence.append(".\t.\n\n")
    with open("output_test.txt", "a") as f:
        for w in list_sequence:
            f.write(w)



def main(train, test):
    list_observe_tag = reformat(train)[0]
    list_observe = reformat(train)[1]
    list_tag = reformat(train)[2]

    dict_observe_prob = prob(list_observe_tag, list_observe, list_tag)[0]
    dict_tran_prob = prob(list_observe_tag, list_observe, list_tag)[1]
    list_tag_unique = prob(list_observe_tag, list_observe, list_tag)[2]
    dict_tag_count = prob(list_observe_tag, list_observe, list_tag)[3]
    #print(len(list_tag_unique))
    # TODO: instead of generating POS for just one sentence, generate POS for all sentences in the test file.
    test_sentence = reformatWordlist(test)[1][0]
        for test_sentence in test_sentences:
        list_v1 = viterbi_initial(test_sentence, dict_observe_prob, dict_tran_prob, list_tag_unique, dict_tag_count)
        list_v, list_back = viterbi_recursion(test_sentence, dict_observe_prob, dict_tran_prob, list_tag_unique, dict_tag_count, list_v1)
        viterbi_end(test_sentence, dict_tran_prob, list_tag_unique, dict_tag_count, list_v, list_back)

    #print(test_sentence)
    # calculate initial value
    list_v1 = viterbi_initial(test_sentence, dict_observe_prob, dict_tran_prob, list_tag_unique, dict_tag_count)
    #print(list_v1)
    # calculate recursion probability
    list_v, list_back, list_back_tag = viterbi_recursion(test_sentence, dict_observe_prob, dict_tran_prob, list_tag_unique, dict_tag_count, list_v1)
    # calculate end probability, and write things into a file
    viterbi_end(test_sentence, dict_observe_prob, dict_tran_prob, list_tag_unique, dict_tag_count, list_v,list_back)


main(f_train, f_test)
__author__ = 'Markell Thornton'
