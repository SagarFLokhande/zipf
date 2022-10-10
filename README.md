# Zipf's Law.

# Contributors : Sagar F. Lokhande

Zipf's Law states that the most common word in a body of text (example a novel) appears twice as often as the second most common word, thrice as often as the third most common word and so on. That is, rank of a word is inversely proportional to the frequency of its occurence. 

This repository of scripts tally the occurences of frequently used words in a novel and then draws a scatter plot to study if Zipf's Law applies. The scripts are written in Python and executed at the command line. They use argparse, sys, csv, scipy, numpy, pandas and other common Python packages. Some Unix Shell elements are also used. The data is a collection of novels in txt format downloaded from www.gutenberg.org, the famous free e-Library project. 

Further, the scripts verify deviations from Zipf's Law by fitting a curve to the data (a model that uses maximum likelihood estimation). The results are included in the repository. 

Here is a brief description of what each script does: 

A. Important

1. countwords.py :
This is a Python script to be executed at the command line. It takes a txt file as input and returns the list of most common words as a dictionary or as a csv on the command line itself. This list is then directed to the results folder and saved as csv.

2. utilities.py : 
A Python module that is very important for our analysis. It describes a function that takes a collection (for example of words) and outputs n most frequent words in csv format. 

3. plotcounts.py : 
Most important Python script in this repository. It draws a scatter plot of our results and describes a model that fits the data. The model uses likelihood estimation and fits a power law that approximates Zipf's Law very well. Finally it plots the empirical results and the model. This script is executed at the command line, takes a csv file and has the option to name the resulting plot. 


B. Not Important

1. book_summary.sh : 
This is a Unix Shell script that takes a novel.txt and extracts a list authors, titles and release dates. These are then saved in separate files in ./results/ folder.

2. script_template.py : 
This is a simple Python script which describes a command that can receive an input file at the terminal and states the name of the output file and the format it should be saved in.

3. collate.py :
This Python script collates most frequent words across novels. It is not used much in our analysis.

4. count_script.py :
This is not a command line script, but a Python function. It takes a txt file and gives n most frequent words as a dictionary or a csv file. 

