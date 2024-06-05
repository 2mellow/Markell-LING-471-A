__author__ = 'Markell Thornton'
#------------------------
#Programming activity 1
#Consider a task of classifying tweets as political or not
#1 = political
#0 = not political
#You have 10 tweets, and the ground truth is:
ground_truth = [1, 1, 0, 1, 0, 0, 1, 1, 0, 1]
#If "political" means "positive",
#Calculate accuracy, precision, and recall if your system outputs:
prediction1 = [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]

#To Do:
accuracy = (4 + 4) / (4 + 4 + 1 + 1) = 0.8 #(TP + TN) / (TP + TN + FP + FN)
precision = 4 / (4 + 1) = 0.8 #TP / (TP + FP)
recall = 4 / (4 + 1) = 0.8 #TP / (TP + FN)

#If you have more time:
prediction2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
prediction3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
prediction4 = [1, 1, 0, 1, 0, 0, 1, 1, 0, 1]
#If you even more:
#Treate "non-political" as "positive"
#And calculate accuracy, precision, and recall
#Think about how to avoid writing repetitive code for differen conditions and different lists.
#if we regard "political" as positive
relevant_class = 0
predict_list = prediction1
true_pos = sum(1 for x, y in zip(ground_truth, predict_list) if (x==y) and (y == relevant_class))
true_neg = sum(1 for x, y in zip(ground_truth, predict_list) if (x==y) and (y != relevant_class))
false_pos = sum(1 for x, y in zip(ground_truth, predict_list) if (x!=y) and (y == relevant_class))
false_neg = sum(1 for x, y in zip(predict_list, ground_truth) if (x!=y) and (y == relevant_class))

precision = true_pos/(true_pos + false_pos)
recall = true_pos/(true_pos + false_neg)


#------------------------
#Programming activity 2
class reviewVec:
    def __init__(self, text, correct_label, prediction):
        self.text = text
        self.correct_label = correct_label
        self.prediction = prediction
#To do:
#Create a reviewVec object
#Assign its attributes to the following values:
#text = "This movie is epic!"
#correct_label = "positive"
#prediction = "negative"
#Print out the text, correct_label, and prediction of this reviewVec object
new_review = reviewVec("This movie is epic!", "positive", "negative")
new_review.text
new_review.correct_label
new_review.prediction

print(new_review.text)           # Output: This movie is epic!
print(new_review.correct_label)  # Output: positive
print(new_review.prediction)     # Output: negative

#------------------------
from pathlib import Path

#Programming activity 3
#Download the tiny-test folder for assignment 3 (you can find it in the 04-23-24 demo folder on GitHub repo as well)
#Create two lists
#hw3_neg: store the full path of all the files in the hw3-neg folder
#hw3_pos: store the full path of all the files in the hw3-pos folder
#TO DO: find the path to the tiny-test folder, and pass it to the Path() method
folder_path_neg = Path(tiny-test/hw3-pos)
folder_path_pos = Path(tiny-test/hw3-neg)
hw3_neg = [file.stem for file in (folder_path / 'hw3-neg').glob('*.txt')]
hw3_pos = [file.stem for file in (folder_path / 'hw3-pos').glob('*.txt')]

#If you have more time: store only the filename, rather than the full path to these two lists
#Instead of having to store the path to neg and pos,
# only store the path to the tiny-test folder,
# then use Path(,) or path1/path2 to navigate to the subfolders
#hw3_pos = [‘g1.txt’, ’g2.txt’, ‘g3.txt’, ‘g4.txt’]
#Hint: Use list comprehension and the .stem method for Path.

p_pos = Path(r'tiny-test/hw3-pos')
p_neg = Path(r'tiny-test/hw3-neg')

#Any files and folders in this path
list(p_neg.glob('*.txt'))
list(p_pos.glob('*.txt'))
#Store all Python files in this path to a list using list comprehension
files_pos = [x for x in p_pos.glob('*.txt') if x.is_file()]
files_neg = [x for x in p_neg.glob('*.txt') if x.is_file()]
