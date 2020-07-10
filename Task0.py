import csv

with open('./texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    print("First record of texts, {} texts {} at time {}".format(*texts[0]))

with open('./calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(*calls[-1]))

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

"""
TASK 0:

O(2) simply O(1)

This is at worst constant time because it always performs two operations
(ignoring the parsing of the file that can be optimized by bailing after reading the first/last line)

* all explanations ignore parsing the csv file
"""
