from variables import *

verification_object = Verification()


def cyclic_values(arr):
    for i in range(len(arr)):

        if i == index_right_word:
            true_right_word = arr[index_right_word]
            return True

        if i == index_summary_index:
            true_summary_index = arr[index_summary_index]
            return True

        if i == index_switch_on:
            true_switch_on = arr[index_switch_on]
            return True

cyclic_values(verification_object.__dict__())
cyclic_values(verification_object.__ver__())

if True:

    received_word = input()


    def word_verification(first_argument, second_argument, third_argument):
        """

        received - Checking the fact that the received_word variable is a string variable and stores a reference to
        'Hello, World!'. return - True : if the received_word variable is a string variable and stores a reference to
        'Hello, World!'. False : if the received_word variable is not a string variable and stores a reference to
        'Hello, World!'.
        """
        if (type(first_argument) == str) and (type(third_argument) == str):
            length_received_word = len(first_argument)

            for i in range(length_received_word):

                if first_argument[i] == third_argument[i]:
                    second_argument = second_argument + 1

                assert first_argument[length_received_word - 1] == '!'
                assert first_argument[length_received_word - 7] == ' '

            if second_argument == length_received_word:
                return True

        return False


    if word_verification(received_word, true_summary_index, true_right_word):
        switch_on = True

    else:
        raise 'Unfortunately, you provided the wrong object reference. Try again!'
