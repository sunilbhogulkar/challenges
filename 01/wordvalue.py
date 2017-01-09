from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as dictionary:
        word_list = [word.replace('\n', '').replace('-', '') for word in dictionary.readlines()]
    return word_list


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[char.upper()] for char in word])


def max_word_value(dictionary=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    score_dict = dict((word, calc_word_value(word)) for word in dictionary)
    return max(score_dict, key=lambda i: score_dict[i])


if __name__ == "__main__":
    print 'The word (from the default DICTIONARY) that has the most value in Scrabble based on LETTER_SCORES is {}'\
        .format(max_word_value())
