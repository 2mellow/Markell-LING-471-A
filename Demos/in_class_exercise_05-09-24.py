__author__ = 'Markell Thornton'

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


df = pd.read_csv("logistic_sample_data.csv",encoding='utf-8')


# Map vowels to numeric values, a as 1; i as 0
vowel_map = {'a': 1, 'i': 0}
color_map = {'a': 'red', 'i': 'blue'}
df['vowel_numeric'] = df['vowel'].map(vowel_map)
df['color'] = df['vowel'].map(color_map)

# Plot
plt.figure(figsize=(4, 3))
for vowel, group in df.groupby('vowel'):
    plt.scatter(group['F1'], group['vowel_numeric'], color=group['color'].iloc[0], label=vowel, alpha=0.6)

plt.yticks([0, 1], ['i', 'a'])
plt.xlabel('F1')
plt.ylabel('Vowel')
plt.legend(title='Vowel')
plt.title('Scatter Plot of Vowel vs. F1')
plt.grid(True)
plt.show()

# Generate probability between 0 to 1
probabilities = np.linspace(0.000001, 0.999999, 100)

# Odd = p / (1-p)
# TODO: Calculate the odds
odds = probabilities / (1 - probabilities)

plt.figure(figsize=(4, 3))
plt.plot(probabilities, odds, label='Odds = p / (1 - p)')
plt.xlabel('Probability (p)')
plt.ylabel('Odds')
plt.title('Relationship between Probability (p) and Odds')
plt.legend()
plt.show()

# Logit = the natural Logarithm of odds
# TODO: calculate the log odds
logit = np.log(odds)

plt.figure(figsize=(4, 3))
plt.plot(probabilities, logit, label='logit = ln(odds)')
plt.xlabel('Probability (p)')
plt.ylabel('Logit')
plt.title('Relationship between Probability (p) and Logit')
plt.legend()
plt.show()

model = smf.logit('vowel_numeric ~ F1', data=df)
result = model.fit()
print(result.summary())

# TODO: based on the intercept and coefficient value, calculate the logit, the odds, and the probability for each datapoint
intercept = result.params['Intercept']
coefficient = result.params['F1']
print(intercept,coefficient)

df['logit'] = intercept + coefficient * df['F1']
df['odds'] = np.exp(df['logit'])
df['probability'] = df['odds'] / (1 + df['odds'])

# Well, you don't necessarily have to write out the whole thing.
df['predicted_prob'] = result.predict(df['F1'])
print(df['predicted_prob'])

# cut off point: p = 0.5
# p/1-p = 1
# ln(1) = 0
# so the cut off F1 frequency is when intercept+coefficient*F1 = 0

F1_cut = -intercept / coefficient
print(F1_cut)

ALPHA = 1

data = pd.read_csv("/content/drive/MyDrive/Colab_Notebooks/my_imdb.csv",encoding='utf-8')
train_data = data[:2]
test_data = data[2:4]

print(train_data)
print(test_data)

# TODO: Set the below 4 variables to contain:
# X_train: the training data; y_train: the training data labels;
# X_test: the test data; y_test: the test data labels.
# Access the data frames by the appropriate column names.

x_train = train_data['review']
y_train = train_data['sentiment']
x_test = test_data['review']
y_test = test_data['sentiment']

'''
# The next three lines are performing feature extraction and word counting.
# They are choosing which words to count frequencies for, basically, to discard some of the noise.
# If you are curious, you could read about TF-IDF,
# e.g. here: https://www.geeksforgeeks.org/tf-idf-model-for-page-ranking/
# What is tf? - Term frequency
# TF(w,d) = Count(w) in document d / total num of words in document d
# What is IDF? - Inversed document frequency

# IDF(w,D) = log( N/1+DF(t) )
# N: Total number of documents in the corpus
# DF(t): Number of documents containing the term 

# The function of IDF: downplay the importance of non-important words such as "the", "a", "and"
# Let's say, the corpus has 100 documents.
# Because these functions words probabily occur in every document in this corpus --> DF(t) = 100
# Then IDF(w,D) = log(100 / 1 + 100)
# For content words, such as "awesome", it occurs in only 2 document in this corpus --> DF(t) = 2
# Then IDF(w,D) = log(100 / 1 + 2)

# Thus, the more frequent a word occur in a corpus, the lower the IDF value is.

# Convert the data into a TF-IDF format means calculating
# TF-IDF(t,d,D)=TF(t,d)×IDF(t,D)
# Thus, if a word occurs frequently in a document, but only in that specific document, the TF-IDF value is high
# If a word occurs frequently in a document, and also occur in all documents in this corpus, the TF-IDF value could be low.

# fit the TfidfVectorizer to the training data (learn the vocabulary and idf statistics) 
# and transform the data into the TF-IDF representation
# or here: https://en.wikipedia.org/wiki/Tf%E2%80%93idf
'''


# TODO: Add a general brief comment on why choosing which words to count may be important.

# Some words might appear more frequently than others when conducting
# a sentiment analysis. For example, in INFO 103, I performed a sentiment analysis on the bias of Reddit comments based on ethical frameworks.

# ngram_range=(1,2) means unigrams and bigrams
tf_idf_vect = TfidfVectorizer(ngram_range=(1, 2))

# Extract features based on the training dataset; Calcualte the TF-IDF score for each feature
tf_idf_train = tf_idf_vect.fit_transform(x_train.values)

# Look for the vocabularies found in the training dataset; Calculate the TF-IDF score of the test dataset based on that
tf_idf_test = tf_idf_vect.transform(x_test.values)

# Check feature names and TF-IDF scores
feature_names = tf_idf_vect.get_feature_names_out()
print(feature_names)
X_train_tfidf_df = pd.DataFrame(tf_idf_train.toarray(), columns=feature_names)
X_test_tfidf_df = pd.DataFrame(tf_idf_test.toarray(), columns=feature_names)

#print(tf_idf_vect)
#print(tf_idf_train)
#print(tf_idf_test)

print("Training Data TF-IDF Matrix:")
print(X_train_tfidf_df)

print("\nTesting Data TF-IDF Matrix:")
print(X_test_tfidf_df)

# Naive Bayes:
# P(pos|Review) = P(Review|pos) * P(pos) / P(review)


# TODO COMMENT: The hyperparameter alpha is used for Laplace Smoothing.
# Add a brief comment, trying to explain, in your own words, what smoothing is for.

# Addresses the potential problem of there being zero probabilities in probabilistic models.

#https://towardsdatascience.com/laplace-smoothing-in-na%C3%AFve-bayes-algorithm-9c237a8bdece

# P(w'|positive) = (number of positive reviews with w') + alpha / N + alpha * K
# N: the number of reviews with y=positive
# alpha: smoothing parameter
# K: numbers of dimensions in the label. In our review, we only have positive and negative, so K should be ?

clf = MultinomialNB(alpha=ALPHA)
clf.fit(tf_idf_train, y_train)
y_pred_train = clf.predict(tf_idf_train)
y_pred_test = clf.predict(tf_idf_test)

print(y_pred_train)
print(y_pred_test)
