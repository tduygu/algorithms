#Count Word Frequency
#Define a function to count the frequency of words in a given list of words.

#Example:

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
#count_word_frequency(words)
#Output:

# {'apple': 3, 'orange': 2, 'banana': 1}


def count_word_frequency(arr):
    words_unq = list(tuple(words))
    word_count = {word:0 for word in words_unq}
    for w in words:
        word_count[w] +=1
    return word_count

print(count_word_frequency(words))