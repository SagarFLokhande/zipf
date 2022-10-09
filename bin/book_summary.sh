# This shell script is part of executables in the study of Zipf law. 
# Here, the script takes a text file denoted by "$1". First it gives the first 17 lines of the header of the file, then it gives the last 8 lines of those 17 lines. Finally, the script searches for the word "$2", specified by the user.  
# Usage: zsh book_summary.sh ../oath/to/file.txt 

for filename in ../data/*.txt
    do
        echo $filename 
        head -n 17 $filename | tail -n 8 | grep "Author"
    done > ../results/authors.txt

for filename in ../data/*.txt
    do 
        echo $filename
        head -n 17 $filename | tail -n 8 | grep "Release Date"
    done > ../results/releases.txt

for filename in ../data/*.txt
    do 
        echo $filename
        head -n 17 $filename | tail -n 8 | grep "Title"
    done > ../results/titles.txt
