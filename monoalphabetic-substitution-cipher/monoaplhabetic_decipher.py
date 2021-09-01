"""
The script deciphers the monoalphabetic ciphers using the crpytoanalysis techniques.
Although efficient, the technique may fail for short or specialized messages.
"""


def building_english_dict():
    """Builds and returns a dictionary consisting of percentages of english letter 
    frequencies in a sample of more than 100,000 documents, newspapers etc compiled by 
    H. Beker and F. Piper, and originally published in 
    Cipher Systems: The Protection Of Communication

    Returns:
        dict: percentages of english letters frequencies
    """
    english_letters_frequency = dict()

    # assigning the percentages of english letters in a sample
    english_letters_frequency['a'] = 8.2
    english_letters_frequency['b'] = 1.5
    english_letters_frequency['c'] = 2.8
    english_letters_frequency['d'] = 4.3
    english_letters_frequency['e'] = 12.7
    english_letters_frequency['f'] = 2.2
    english_letters_frequency['g'] = 2.0
    english_letters_frequency['h'] = 6.1
    english_letters_frequency['i'] = 7.0
    english_letters_frequency['j'] = 0.2
    english_letters_frequency['k'] = 0.8
    english_letters_frequency['l'] = 4.0
    english_letters_frequency['m'] = 2.4
    english_letters_frequency['n'] = 6.7
    english_letters_frequency['o'] = 7.5
    english_letters_frequency['p'] = 1.9
    english_letters_frequency['q'] = 0.1
    english_letters_frequency['r'] = 6.0
    english_letters_frequency['s'] = 6.3
    english_letters_frequency['t'] = 9.1
    english_letters_frequency['u'] = 2.8
    english_letters_frequency['v'] = 1.0
    english_letters_frequency['w'] = 2.4
    english_letters_frequency['x'] = 0.2
    english_letters_frequency['y'] = 2.0
    english_letters_frequency['z'] = 0.1

    return english_letters_frequency



if __name__ == '__main__':
    """
    1. Read data
    2. calculate frequency
    3. replace most reccuring letters
    4. check for vowel / consonents
    5. re-generate what we already know about the cipher
    """