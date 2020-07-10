import csv

# numbers that make outgoing calls
# but never send texts, receive texts or receive incoming calls
POSSIBLE_TELEMARKETER = { 'call_out': True, 'call_in': False, 'text_out': False, 'text_in': False }


def new_caller():
    return { 'call_out': True, 'call_in': False, 'text_out': False, 'text_in': False }
def new_called():
    return { 'call_out': False, 'call_in': True, 'text_out': False, 'text_in': False }


phones = {}
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for caller, receiver, _, _ in calls:
        if caller in phones:
            phones[caller]['call_out'] = True
        else:
            phones[caller] = new_caller()

        if receiver in phones:
            phones[receiver]['call_in'] = True
        else:
            phones[receiver] = new_called()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    # Only update phones involved in calls, can be updated to include texts
    for texter, texted, _ in texts:
        if texter in phones:
            phones[texter]['text_out'] = True
        if texted in phones:
            phones[texted]['text_in'] = True


possible_telemarketers = []
for phone, meta_data in phones.items():
    if meta_data == POSSIBLE_TELEMARKETER:
        possible_telemarketers.append(phone)

print("These numbers could be telemarketers: ")
for possible_telemarketer in sorted(possible_telemarketers):
    print(possible_telemarketer)


"""
TASK 4:

worst: O(2n + n log n)
simply: O(n log n)

n = the number of lines in both csv files.

Two loops gather data. They populate the dataset with number metadata for callers/called phones.

List sort is O(n log n)
We are sorting a subset of n, the worst case is n. This is the slowest part of the solution.
"""

"""
TASK 4:
The telephone company wants to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
