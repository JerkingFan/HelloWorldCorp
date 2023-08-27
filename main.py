import time


received_word = input()
right_word = 'Hello, World!'
summary_index = 0

switch_on = False

def word_verification(first_argument, second_argument, third_argument):
    '''

    received - Checking the fact that the received_word variable is a string variable
                    and stores a reference to 'Hello, World!'.
    return - True : if the received_word variable is a string variable and stores a reference to 'Hello, World!'.
            False : if the received_word variable is not a string variable and stores a reference to 'Hello, World!'.
    '''
    if (type(first_argument) == str) and (type(third_argument) == str):
        length_received_word = len(first_argument)


        for i in range(length_received_word):

            if first_argument[i] == right_word[i]:

                second_argument = second_argument + 1

            assert received_word[length_received_word-1] == '!'
            assert received_word[length_received_word-7] == ' '


        if second_argument == length_received_word:

            return True

    return False



if word_verification(received_word, summary_index, right_word) == True:

    switch_on = True

else:
    raise Exception('Unfortunately, you provided the wrong object reference. Try again!')