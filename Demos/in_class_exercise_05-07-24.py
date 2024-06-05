__author__ = 'Markell Thornton'

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as statsm

# Part 1
# the data file
data = [
[1, 9.901309],
[2,	9.159132],
[3,	10.769071],
[4,	10.625958],
[5,	10.016544],
[6,	9.220177],
[7,	10.296991],
[8,	10.010818]]

df = pd.DataFrame(data, columns=['x', 'y_data'])

# TODO: calculate the sse when only estimating the intercept; i.e. y_estimate = 10
# all predicted value is 10
intercept = 10
predicted_values = [intercept] * len(df['x'])

# Calculate squared error
squared_errors = [(y - intercept) ** 2 for y in df['y_data']]

# calcuate the sum of it
sse = sum(squared_errors)
print(f"SSE when y_estimate = 10: {sse:.4f}")

# Draw a plot
# First, draw out the scatterplot
# Then add lines of y = 12, 9, 10
plt.scatter(df["x"], df["y_data"], color='blue', label='original data')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(7, 13)

# plot the x and predicted value on the plot
# intercept = 12
plt.plot(df["x"], [12] * len(df["x"]) , label='Line', color='orange')

# TODO: add a line where intercept = 9
plt.plot(df["x"], [9] * len(df["x"]), label='Intercept = 9', color='green')

# TODO: add a line where intercept = 10
plt.plot(df["x"], [10] * len(df["x"]), label='Intercept = 10', color='red')

plt.legend()
plt.show()

# Part 2
# the data file with slope and intercept
# the data file
data = [
[0,	5.080128],
[1,	6.924483],
[2,	6.731348],
[3,	9.304862],
[4,	13.22064],
[5,	13.98692],
[6,	17.31106],
[7,	16.5803],
[8,	18.86026]]

df = pd.DataFrame(data, columns=['x', 'y_data'])

# let's use the formula provided in slides and check if the formula yields the same result as the sklearn module
nominator_array = (df['x']-np.mean(df['x'])) * (df['y_data'] - np.mean(df['y_data']))
nominator = np.sum(nominator_array)

denominator_array = (df['x']-np.mean(df['x']))**2
denominator = np.sum(denominator_array)

print(nominator)
print(denominator)

slope = nominator/denominator

print(slope)

# TODO: fit intercept and slope
#convert x into matrix shape
x = df['x'].values.reshape(-1,1)
y = df['y_data'].values
reg = LinearRegression()
mod = reg.fit(x, y)
model_coef = mod.coef_[0]
model_intercept = mod.intercept_
print(model_coef) # get slope
print(model_intercept) # get intercept;

# Draw the scatter plot and fit the modeled line
# initiate the scatter plot with the x value and y value for each point
plt.scatter(df["x"], df["y_data"], color='blue', label='original data')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(0, 25)

# plot the x and predicted value on the plot
# model output
# TODO: fill in the x and y value to plot a line
plt.plot(df["x"], slope_manual * df["x"] + intercept_manual, color='orange', label='Manual fit')
plt.plot(df["x"], model_coef * df["x"] + model_intercept, color='green', linestyle='dashed', label='scikit-learn fit')

plt.legend()
plt.show()


# Part 3
# Real-world linguistics data

df.vowel_pitch = pd.read_csv("linear_regression_data.csv",encoding='utf-8')
x = df.vowel_pitch['F1']
y = df.vowel_pitch['f0']

# feed it to linear regression method
x = x.values.reshape(-1,1)
y = y.values

# TODO: fill in regression (reg) and model (mod)
reg = LinearRegression()
mod = reg.fit(x, y)

# Get the slope
model_coef = mod.coef_[0]
model_intercept = mod.intercept_
print(f"The slope is: {model_coef}") # get slope
print(f"The intercept is: {model_intercept}") # get intercept;


# TODO: Draw scatter plot and the fitted line
# Fill in the plt.scatter()
plt.scatter (plt.scatter(df_vowel_pitch['x'], df_vowel_pitch['y'], color='red', label='Original data')
plt.xlabel('x')
plt.ylabel('y')

# plot the x and predicted value on the plot
# model output
# Fill in the plt.plot()
plt.plot(df_vowel_pitch['F1'], model_coef * df_vowel_pitch['F1'] + model_intercept, color='orange', label='Fitted line')

plt.legend()
plt.show()
