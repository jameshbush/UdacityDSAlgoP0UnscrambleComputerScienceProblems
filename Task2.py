import csv

DURATION_INDEX = 1

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    totals = {}
    for caller, receiver, _, duration in calls:
        assert(caller != receiver)
        totals[caller] = totals.get(caller, 0) + int(duration)
        totals[receiver] = totals.get(receiver, 0) + int(duration)

    max = ('', 0)
    for total in totals.items():
        if total[DURATION_INDEX] > max[DURATION_INDEX]:
            max = total

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(*max))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

"""
TASK 2:

best: O(n + 2)
worst: O(n + n*2) or O(3n)
simply: O(n)

The first loop operates at constant time, assigning durations to a dictionary.
The second loop depends on how many overlapping phone numbers there are.
It's possibilities range from a best case scenario where two people call each other every time,
to a worst case scenario where no overlap exists.

Because the range between n and 3n is trivial compared to quadratic time, this is simplified N = O(n)
"""
