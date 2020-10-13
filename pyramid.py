from collections import Counter

def is_pyramid_word(text: str) -> bool:
    """
    This method tests if a word is pyramid word. A word is pyramid when the letters can be arrange in increasing frequency.
    :param text: a string
    :return: returns 
    """
    #check input for string
    if type(text) != str:
        return False
    #eliminate whitespaces, tabs and new lines
    text = text.translate(str.maketrans('', '', ' \n\t\r'))
    #check for empty string
    if len(text) == 0:
        return False
    #initialize a counter
    word_count = Counter()
    #traverse the string to get letters
    for letter in text:
        word_count[letter] += 1
    # sorting count of letters
    sorted_count = sorted(word_count.values())
    # compare index and num, if they don't differ by one, the word is not a pyramid
    for i, num in enumerate(sorted_count):
        if num - i != 1:
            return False
    return True