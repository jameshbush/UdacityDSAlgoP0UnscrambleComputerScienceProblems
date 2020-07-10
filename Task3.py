import csv
import re

AREA_CODE_REGEX = '^\d*'
FIXED_LINE_REGEX = '^\(\d*'


def is_bangalore_fixed(phone):
  return phone[0:5] == '(080)'

def match_area_code_or_prefix(phone):
  fixed = re.match(FIXED_LINE_REGEX, phone)
  if fixed:
    return fixed.group()[1:]
  else:
    return re.match(AREA_CODE_REGEX, phone).group()

def add_area_code(area_code):
  area_codes_and_mobile_prefixes_called_by_bangalorians.add(area_code)


area_codes_and_mobile_prefixes_called_by_bangalorians = set()
calls_from_bangalore, calls_from_to_bangalore = 0, 0

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for caller, receiver, _, _ in calls:
      if is_bangalore_fixed(caller):
        calls_from_bangalore += 1
        add_area_code(match_area_code_or_prefix(receiver))
        if is_bangalore_fixed(receiver):
          calls_from_to_bangalore += 1


# A
area_codes_and_mobile_prefixes_called_by_bangalorians = sorted(list(area_codes_and_mobile_prefixes_called_by_bangalorians))
print("The numbers called by people in Bangalore have codes:")
for phone in area_codes_and_mobile_prefixes_called_by_bangalorians:
  print(phone)

# B
print("{0:.2%} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
.format(calls_from_to_bangalore / calls_from_bangalore))


"""
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
"""


"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
