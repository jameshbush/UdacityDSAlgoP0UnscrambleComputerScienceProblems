## Udacity intro to data structures

This is my Big O time complexity analysis of various solutions. My work and answers here are my own. This is not a tutorial.


TASK 0:

O(2) simply O(1)

This is at worst constant time because it always performs two operations
(ignoring the parsing of the file that can be optimized by bailing after reading the first/last line)

* all explanations ignore parsing the csv file


TASK 1:

O(2n+2) simply O(n)

This is at worst (and always) linear time because we perform two operations on every element of the list.
We first access the an element of the set, then append it to another set.


TASK 2:

best: O(n + 2)
worst: O(n + n*2) or O(3n)
simply: O(n)

The first loop operates at constant time, assigning durations to a dictionary.
The second loop depends on how many overlapping phone numbers there are.
It's possibilities range from a best case scenario where two people call each other every time,
to a worst case scenario where no overlap exists.

Because the range between n and 3n is trivial compared to quadratic time, this is simplified N = O(n)


TASK 3:

worst: O(2n + n log n)
simply: O(n log n)

One loop gathers data.
If the caller is from Bangalore, we captures receiver area code.
We count Bangalore calls. We also counts if calls were to Bangalore.

List instantiation is O(n)
where n is between 0 and the original n depending on how many elements met our filter criteria.

List sort is O(n log n)
This is slower than constant time, but faster than quadratic time.
Python sorts list using a variation of Mergesort, which has a bad but unavoidable time complexity.
We have optimized this operation responsibly by filtering duplicates.


TASK 4:

worst: O(2n + n log n)
simply: O(n log n)

n = the number of lines in both csv files.

Two loops gather data. They populate the dataset with number metadata for callers/called phones.

List sort is O(n log n)
We are sorting a subset of n, the worst case is n. This is the slowest part of the solution.
