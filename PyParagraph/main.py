"""This script will open files of existing employee information and reformat them"""

import os
import re

paragraph = ""
words = []
word_count = 0
sentences = []
sentence_count = 0
words_per_sentence = 0
total_letters = 0
word_length = 0

# open csv file
filename = input("Please enter the filename for the paragraph you would like to review: ")
filepath = os.path.join("raw_data",filename)

with open(filepath, 'r', newline="") as text:
    paragraph = text.read()
    words = paragraph.split(" ")
    sentences = re.split("[\.\!\?]\s", paragraph)
    word_count = len(words)
    sentence_count = len(sentences)
    words_per_sentence = word_count/sentence_count

    for character in paragraph:
        if character.isalpha() == True:
            total_letters = total_letters + 1
    
    word_length = total_letters/word_count

# return results
print("Paragraph Analysis")
print("-----------------")
print(f"Approximate Word Count: {word_count}")
print(f"Approximate Sentence Count: {sentence_count}")
print(f"Average Letter Count: {word_length}")
print(f"Average Sentence Length: {words_per_sentence}")