__author__ = 'Markell Thornton'
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''
Examples: Bar plot
'''
# Sample data for three series
categories = ['The', 'cat', 'chase', 'dog']
values = [1781580, 428363, 556892, 1131181]

# Create a DataFrame
df = pd.DataFrame({
    'Category': categories,
    'Value': values,
})

# Plot the stacked bar plot
plt.bar(df['Category'], df['Value'], label = "values")

# Add title and labels
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')

# Show the plot
plt.show()

'''
Example: Grouped bar plots
'''
categories = ['train_accuracy_pos', 'train_precision_pos', 'train_recall_pos', 'train_precision_neg', 'train_recall_neg',
              'test_accuracy_pos', 'test_precision_pos', 'test_recall_pos', 'test_precision_neg', 'test_recall_neg']
original = np.random.rand(10)
clean = np.random.rand(10)
lowercase = np.random.rand(10)
no_stop = np.random.rand(10)
lemmatized = np.random.rand(10)

# Create a DataFrame
df = pd.DataFrame({
    'category': categories,
    'original': original,
    'clean': clean,
    'lowercase': lowercase,
    'no_stop': no_stop,
    'lemmatized': lemmatized
})

# Width of each bar
bar_width = 0.15
group_gap = 0.5

# Set position of bars on X axis
bar_positions = np.arange(len(df['category'])) + 5
bar1 = bar_positions
bar2 = bar1 + bar_width
bar3 = bar1 + 2 * bar_width
bar4 = bar1 + 3 * bar_width
bar5 = bar1 + 4 * bar_width

# Create the figure
plt.figure(figsize=(14, 8))
# Plot the bars
plt.bar(bar1, df['original'], color='b', width=bar_width, edgecolor='grey', label='Original')
plt.bar(bar2, df['clean'], color='g', width=bar_width, edgecolor='grey', label='Clean')
plt.bar(bar3, df['lowercase'], color='r', width=bar_width, edgecolor='grey', label='Lowercase')
plt.bar(bar4, df['no_stop'], color='c', width=bar_width, edgecolor='grey', label='No Stop Words')
plt.bar(bar5, df['lemmatized'], color='m', width=bar_width, edgecolor='grey', label='Lemmatized')

# Add title and labels
plt.title('Grouped Bar Plot of Different Text Processing Techniques')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.xticks(bar1 + 2 * bar_width, df['category'], rotation=90)

# Add legend outside the plot
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Adjust layout to make room for the legend
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Show the plot
plt.show()



#----------------------------------------
# Exercises
categories = ['accuracy', 'precision_pos', 'recall_pos', 'precision_neg', 'recall_neg']*2
type = ['train', 'train', 'train', 'train', 'train', 'test', 'test', 'test', 'test', 'test']
values = [0.9736, 0.9833, 0.9635, 0.9642, 0.9836,
          0.8697, 0.9011, 0.8305, 0.8428, 0.9089]

# Create a DataFrame
df = pd.DataFrame({
    'category': categories,
    'type': type,
    'value': values,
})

# TODO: Given the dataset, plot two bar plots, one for train, the other for test
pivot_df = df.pivot(index='category', columns='type', values='value').reset_index()
fig, ax = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

ax[0].bar(pivot_df['category'], pivot_df['train'], color='blue')
ax[0].set_title('Training Data')
ax[0].set_xlabel('Category')
ax[0].set_ylabel('Value')
ax[0].set_xticklabels(pivot_df['category'], rotation=45, ha='right')

ax[1].bar(pivot_df['category'], pivot_df['test'], color='green')
ax[1].set_title('Testing Data')
ax[1].set_xlabel('Category')
ax[1].set_xticklabels(pivot_df['category'], rotation=45, ha='right')

plt.tight_layout()
plt.show()

# TODO: Rearrange the dataset, so that you can group things either by test/train, or by the error analysis values
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35

r1 = np.arange(len(pivot_df.columns[1:]))
r2 = [x + bar_width for x in r1]

transposed_df = pivot_df.set_index('category').transpose().reset_index()

for i, category in enumerate(transposed_df.columns[1:]):
    ax.bar(r1 + i * bar_width, transposed_df[category], width=bar_width, edgecolor='grey', label=category)


ax.set_xlabel('Type', fontweight='bold')
ax.set_ylabel('Value', fontweight='bold')
ax.set_title('Grouped Bar Plot by Error Analysis Values')
ax.set_xticks([r + bar_width for r in range(len(transposed_df))])
ax.set_xticklabels(transposed_df['type'], rotation=45, ha='right')

plt.tight_layout()
plt.show()
