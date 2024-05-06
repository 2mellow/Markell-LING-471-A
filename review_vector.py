'''
A class for review vectors.
'''


class reviewVec:
    def __init__(self, text, correct_label, prediction):
        self.text = text
        self.correct_label = correct_label
        self.prediction = prediction
