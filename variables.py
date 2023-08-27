true_right_word = 'Hello, World!'
true_summary_index = 0
index_right_word = 0
index_summary_index = 1
index_switch_on = 2


class Verification:
    """
    A class that stores variables necessary for initialization and continuation of the 'word_verification' function.
    """

    def __init__(self):
        self.right_word = 'Hello, World!'
        self.summary_index = 0
        self.switch_on = False

    def __dict__(self):
        self.array = []
        self.array.append(self.right_word)
        self.array.append(self.summary_index)
        self.array.append(self.switch_on)
        return self.array

    def __ver__(self):
        self.true_right_word = 'Hello, World!'
        self.true_summary_index = 0
        self.index_right_word = 0
        self.index_summary_index = 1
        self.index_switch_on = 2
        return self.true_right_word, self.true_summary_index
