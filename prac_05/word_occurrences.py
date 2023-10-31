"""
Word Occurrences
Estimate: 15 minutes
Actual:   7 minutes
"""

word_to_count = {}
text = input("Text: ")
words = text.split(sep=" ")
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

maximum_word_length = max(len(word) for word in word_to_count.keys())
for word, count in sorted(word_to_count.items()):
    print(f"{word:{maximum_word_length}} : {count}")
