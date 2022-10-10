# Zipf's Law.

# Contributors : Sagar F. Lokhande

Zipf's Law states that the most common word in a body of text (example a novel) appears twice as often as the second most common word, thrice as often as the third most common word and so on. That is, rank of a word is inversely proportional to the frequency of its occurence. 

This repository of scripts tally the occurences of frequently used words in a novel and then draws a scatter plot to study if Zipf's Law applies. The scripts are written in Python and executed at the command line. They use argparse, sys, csv, scipy, numpy, pandas and other common Python packages. Some Unix Shell elements are also used. The data is a collection of novels in txt format downloaded from www.gutenberg.org, the famous free e-Library project. 

Further, the scripts verify deviations from Zipf's Law by fitting a curve to the data (a model that uses maximum likelihood estimation). The results are included in the repository. 
