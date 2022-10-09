import string
from collections import Counter

def count_words(reader):
    """Count the appearance of each word in a string."""
    text = reader.read()
    chunks = text.split()
    npunc = [word.strip(string.punctuation) for word in chunks]
    word_list = [word.lower() for word in npunc if word]
    word_counts = Counter(word_list)
    return word_counts

with open('dracula.txt', 'r') as reader:
    word_counts = count_words(reader)

#print(word_counts)

import sys
import csv

def collection_to_csv(word_collection, num=None):
    """Write collection of words and their respective counts in csv format"""
    word_collection = word_collection.most_common()
    if num is None:
        num = len(word_collection)
    writer = csv.writer(sys.stdout)
    writer.writerows(word_collection[0:num])

collection_to_csv(word_counts, num=10)


