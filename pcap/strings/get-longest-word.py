#  Assume that words in a string can be separated with spaces, commas, new line characters or full stops.
#  This means that abbreviated forms with apostrophes (e.g. I'm) are considered to be a single word.
def get_longest_word(str):
    w1 = ((str.replace(',', ' ')).replace('.', ' ')).replace('?', ' ')
    words = w1.split()
    len_w = (0 , '')
    for w in words:
        if len_w[0] < len(w):
            len_w = (len(w), w)
    return len_w[1]



sample_story = '''Once upon a time, there was a beginner programmer named Alice who was eager to learn Python. She tried to learn from books, 
but found it difficult to grasp the concepts. One day, she stumbled upon an online course.

Alice was thrilled. The course was taught by a well-known programmer who made the lessons interesting and easy to understand. 
The course covered everything a beginner programmer needed, and Alice was finally able to understand how to code in Python.'''

str2="who knows, well..."
print(sample_story)
print(get_longest_word(sample_story))

print(get_longest_word(str2))

