"""Collection of commonly used functions which may appear as modules in different scripts."""

import sys 
import csv

def collection_to_csv(word_collection, num=None):
    """Write out collection of items and counts in csv format.
    Parameters
    ----------
    word_collection : collections.Counter
        Collection of items (words) and counts
    num : int
        Limit output to N most frequent items
    """
    word_collection = word_collection.most_common()
    if num is None:
        num = len(word_collection)
        
    writer = csv.writer(sys.stdout) 
    writer.writerows(word_collection[0:num])

