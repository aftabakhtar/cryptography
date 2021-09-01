"""
The script deciphers the monoalphabetic ciphers using the crpytoanalysis techniques.
Although efficient, the technique may fail for short or specialized messages.
"""
from rich.console import Console
console = Console()


def read_cipher_alphabet(filename: str) -> str:
    """Reads the cipher text from text file

    Args:
        filename (str): the name of file containing cipher text

    Returns:
        str: the string consisting of the cipher text
    """
    file_openend = open(filename)

    return file_openend.read()


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


def calculate_frequencies(cipher_text: str) -> dict:
    """Caclulates the frequencies of characters in the cipher text

    Args:
        cipher_text (str): the cipher text to decipher

    Returns:
        dict: frequencies of different characters in the cipher
    """
    cipher_frequencies = dict()
    for character in cipher_text:
        try:
            cipher_frequencies[character] += 1
        except KeyError:
            cipher_frequencies[character] = 1
    
    return cipher_frequencies


def sort_dictionary(dictionary: dict) -> dict:
    return {k: v for k, v in reversed(sorted(dictionary.items(), key=lambda item: item[1]))}


def initial_analysis(cipher_text: str, english_frequency: dict, cipher_frequency: dict):
    frequent_cipher_letter = []
    frequent_english_letter = []
    del cipher_frequencies[' ']

    for key in sort_dictionary(cipher_frequencies):
        frequent_cipher_letter += [key]

    for key in sort_dictionary(english_frequency):
        frequent_english_letter += [key]

    console.print('Replacing 3 most frequent Cipher letters with most frequent English letters respectively', style='bold red')
    
    for i in range(3):
        for j in range(3):
            console.print(f'Replacing {frequent_cipher_letter[i]} with {frequent_english_letter[j]} in the Cipher text', style='green')
            console.print(cipher_text.replace(frequent_cipher_letter[i], frequent_english_letter[j]))
            print()



if __name__ == '__main__':
    """
    1. Read data
    2. calculate frequency
    3. replace most reccuring letters
    4. check for vowel / consonents
    5. re-generate what we already know about the cipher
    """
    cipher_text = read_cipher_alphabet('./monoalphabetic-substitution-cipher/cipher_text')
    cipher_frequencies = calculate_frequencies(cipher_text)
    initial_analysis(cipher_text, building_english_dict(), cipher_frequencies)
