"""
Chris Reppel
Prac 5
2/4/19
"""

count_words = {}
text = input("Text: ")
words = text.split()
for word in words:
    occurrence = count_words.get(word, 0)
    count_words[word] = occurrence + 1

words = list(count_words.keys())
words.sort()

length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, length, count_words[word]))
