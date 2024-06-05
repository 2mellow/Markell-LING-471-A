import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

'''
Review: Precision and Recall
Imagine you are a data scientist working on a language model designed to detect hate speech in tweets. 
You have randomly selected 120 tweets from a dataset to test your model. 
Your task is to evaluate the performance of the model based on the following results:

               | Predicted: Yes | Predicted: No | Predicted: None
---------------|----------------|---------------|---------------
Actual: Yes    | 30             | 20            | 5
Actual: No     | 10             | 40            | 15


Please calculate the accuracy, precision, recall accuracy of this model for 
correctly detecting non-hate speech

'''
true_pos = 40
true_neg = 20
false_pos = 30
false_neg = 10
accuracy = (true_pos + true_neg) / (true_pos + true_neg + false_pos + false_neg)
precision = true_pos / (true_pos + false_pos)
recall = true_pos / (true_pos + false_neg)

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")

def normal_pdf(x, mu, sigma):
    # mu: the mean
    # sigma: the standard deviation
    # square root: np.sqrt()
    # exponent of e: np.exp()

    # TODO: delete "None", and assign values to the coefficient and exponent
    coefficient = 1 / (sigma * np.sqrt(2 * np.pi))
    exponent = -0.5 * ((x - mu) / sigma) ** 2
    return coefficient * np.exp(exponent)

def normal_cdf(x, mu, sigma):
    return 0.5 * (1 + erf((x - mu) / (sigma * np.sqrt(2))))

# Calculate the probability within 1 sd of the mean
prob_within_one_sd = normal_cdf(1, 0, 1) - normal_cdf(-1, 0, 1)

# TODO: Calculate the probability within 2 sd of the mean
prob_within_two_sd = normal_cdf(2, 0, 1) - normal_cdf(-2, 0, 1)

# TODO: Calculate the probability within 3 sd of the mean
prob_within_three_sd = normal_cdf(3, 0, 1) - normal_cdf(-3, 0, 1)

print(prob_within_one_sd)
print(prob_within_two_sd)
print(prob_within_three_sd)

# Plot out pdf and cdf
x_data = np.linspace(-5, 5, 1000)

# Use the function for pdf defined above to calculate y_data_pdf
y_data_pdf = normal_pdf(x_data, 0, 1)

normal_pdf(x, mu, sigma)

# Use the function for cdf defined above to calculate y_data_cdf
y_data_cdf = normal_cdf(x_data, 0, 1)

# Plot pdf
plt.plot(x_data, y_data_pdf, label='PDF')
# Plot cdf
plt.plot(x_data, y_data_cdf, label='CDF')
plt.legend()
plt.show()
