"""
Estimated = 20 minutes
Actual = 30 minutes
"""


text = input("text: ")
words = text.split()
word_to_count = {}

for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

max_length = max((len(word) for word in words))
for word in sorted(word_to_count):
    print(f"{word:{max_length}} : {word_to_count[word]}")