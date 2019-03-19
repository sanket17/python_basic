


def say_hello():
    '''
    DOCSTRING: Prints hello world.
    INPUT: no input
    OUTPUT: Hello World
    '''
    print('Hello World')

say_hello()

#solving PIG LATIN problem
def check_pig_latin(word):
    '''
    DOCSTRING: Pig Latin problem, if a word starts with a vowel append 'ay' to it.
                If word doesnot starts with vowel, then remove first letter and add that letter to end appending ay after it.
    INPUT: word
    OUTPUT: word -> ordway
            apple -> appleay
    '''
    if word[0].lower() in 'aeiou':
        pig_latin_word = word + 'ay'
    else:
        pig_latin_word = word[1:] + word[0] + 'ay'
    print('PIG LATIN WORD - {}'.format(pig_latin_word))

check_pig_latin('word')
check_pig_latin('apple')
