# length_encoding.py

You are given a text file text.txt 

You will need to use run length encoding on all lines and remove any repeated lines.

Then sort all lines with the first number from largest to smallest and save the output to a new file named encoded_text.txt

(Note: if two or more lines have the same first number, we don't care about the order of them) 
 
Example: 

aaabcc

abbbcccd

aabbc

aaabcc

aabbcc
 
output:

3a1b2c

2a2b1c

2a2b2c

1a3b3c1d


