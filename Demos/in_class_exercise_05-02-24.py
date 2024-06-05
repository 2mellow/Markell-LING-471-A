__author__ = 'Markell Thornton'

# TODO 1
'''
Imagine that you are learning Spanish.
# You want to estimate the likelihood that a noun is feminine.
# Your prior belief, based on the vocabularies that you have learnt in Spanish,
# is that about 46% of the words are feminine.
# 𝑃(𝐹)=0.46
# Now, your language teacher told you that out of the feminine words,
# 80% of them end in “-a”
# 𝑃(𝑎│𝐹)=0.8
# And based on corpus data, you know that 60% words end in “-a” in Spanish.
# 𝑃(𝑎)=0.6
# Using Bayes' theorem, you want to update your belief about
# when you see a word ending in “-a”, what is the likelihood that this word is feminine
'''

# What you want to know (posterior probability): P(F|a) -- The likelihood that a word is feminine if it ends in "a"
# What you know (your prior knowledge): P(F) -- The likelihood that a word is feminine
# What else you know (your prior knowledge): P(a) -- In a Spanish corpus that you found, 60% of words ends in "a"
# What is the new knowledge you learnt (likelihood): P(a|F) -- In Spanish, 80% of the feminine words ends in "a"
# Now, Let's use Bayes' theorem to get P(F|a)

p_F = 0.46
p_a_given_F = 0.8
p_a = 0.6


p_F_given_a = (p_a_given_F * p_F) / p_a #Bayes' theorem P(F|a)

print(f"The likelihood that a word is feminine given that it ends in 'a' (P(F|a)) is: {p_F_given_a}")

# TODO 2
'''
Suppose
1% of people have cancer;
Out of the people who truly have cancer and get tested, 80% of these tests detect cancer correctly;
Out of the people who do not have cancer and get tested, 9.6% of these tests still return a cancer-positive results.

Question: If you get a positive result, what is the probability you actually have cancer?
'''

# What we want to know: P(cancer | positive) -- given a positive result, the probability of having cancer
# What you already know: P(cancer) -- the probability of a person has cancer
# What you learnt: P(positive|cancer) -- given someone has cancer, the probability they get a positive result
# What you also learnt: P(positive|no cancer) -- given someone does not have cancer, the probability they get a positive result

p_cancer = 0.01
p_positive_given_cancer = 0.80
p_positive_given_no_cancer = 0.096

# So we still need P(positive). How to get that?

# Remember joint probability P(A and B) and marginal probability P(A)?
# If we add all the possible joint probability for event A,
# we are going to get the marginal probability for P(A)
# So you can either have cancer, or not have cancer.
# If we add these two outcomes together, we get the probability of having cancer
# So, P(positive) = P(positive and cancer) + P(positive and no cancer)

# Remember the definition of conditional probability? P(A|B) = P(A and B) / P(B)
# Accordingly, P(A and B) = P(A|B) * P(B)
# P(positive and cancer) = P(positive|cancer) * P(cancer)

p_positive_and_cancer = p_positive_given_cancer * p_cancer

# P(positive and no cancer) = P(positive|no cancer) * P(no cancer)
p_no_cancer = 1 - p_cancer
p_positive_and_no_cancer = p_positive_given_no_cancer * p_no_cancer

# P(positive) = P(positive and cancer) + P(positive and no cancer)
p_positive = p_positive_and_cancer + p_positive_and_no_cancer


#OK, now we are done
# P(cancer|positive) = P(positive|cancer)*P(cancer) / P(positive)

p_cancer_given_positive = (p_positive_given_cancer * p_cancer) / p_positive

print(p_cancer_given_positive)

# TODO 3
'''
You have made an auto suggest feature for a keyboard
The user has entered "to the" and you need to suggest the next word
In your corpus, "to the X" appears in 3854 out of 1,640,329 trigrams
Of these "to the other" appears 33 times, and "to the wrong" appears 27 times
If a user entered "to the", what is the probability the next word user enters is "other"? What about "wrong"?
'''

# What we want to know (posterior probability): P(other|to the) and P(wrong|to the)
# What we know: P(to the X)
# What we know: P(to the other) <=> P(to the & other)
# What we know: P(to the wrong) <=> P(to the & wrong)

p_to_the_other = 33 / 1640329
p_to_the_wrong = 27 / 1640329
p_to_the = 3854 / 1640329 

p_other_given_to_the = p_to_the_other / p_to_the
p_wrong_given_to_the = p_to_the_wrong / p_to_the

print(p_other_given_to_the)
print(p_wrong_given_to_the)

# TODO 4
# Using Pandas to create dataframe
# Make use of the cleanFileContents() function to read the file content
'''
Task: store the files in your tiny-test folder into the following format:

  file label       type                           review
0   g2   pos  tiny-test      good good good bad bad bad 
1   g4   pos  tiny-test                            good 
2   g3   pos  tiny-test  good good good bad bad bad bad 
3   g1   pos  tiny-test          good good good bad bad 

'''

from pathlib import Path
import re
import string
import pandas as pd

def cleanFileContents(f):
    with open(f, 'r', encoding='utf-8') as f:
        text = f.read()
    clean_text = text.translate(str.maketrans('', '', string.punctuation))
    clean_text = re.sub(r'\s+', ' ', clean_text)
    clean_text = clean_text
    return clean_text

# Step 1: Get path from tiny-test/hw3-pos and tiny-test/hw3-neg

path_pos = Path('tiny-test/hw3-pos')
path_neg = Path('tiny-test/hw3-neg')

# Step 2: Read files and folders in this path

filelist_pos = [f for f in path_pos.glob('*.txt')]
filelist_neg = [f for f in path_neg.glob('*.txt')]

# Create two lists using list comprehension. Each file should have its separate lists.
# We are creating a row for each file.
# it should be the name of the file, pos/neg, train or test, and the content of the review
# Hint: use list comprehension
filelist_pos_list = [
    [file.stem, 'pos', 'tiny-test', cleanFileContents(file)] for file in filelist_pos]
filelist_neg_list = [
    [file.stem, 'neg', 'tiny-test', cleanFileContents(file)] for file in filelist_neg]

# Combine the pos and neg lists together
filelist_list = filelist_pos_list + filelist_neg_list

# Assign column names to the four columns
column_names = ['file', 'label', 'type', 'review']

# Use the method DataFrame in pandas to create a dataframe
df = pd.DataFrame(data=filelist_list, columns=column_names)

print(df)
