import csv
import re

SENDING = 0

numbers = set()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    for text in texts:
        numbers.add(text[0])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        numbers.add(call[0])

print("There are %d different telephone numbers in the records." % len(numbers))

# note: length == 517 stripped or raw so data clean

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

"""
TASK 1:

O(2n+2) simply O(n)

This is at worst (and always) linear time because we perform two operations on every element of the list.
We first access the an element of the set, then append it to another set.
"""
