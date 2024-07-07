from collections import Counter

data = [{'item': 'item1', 'amount': 400}, 
        {'item': 'item2', 'amount': 300}, 
        {'item': 'item1', 'amount': 750}]

counter = Counter()
for d in data:
    counter[d['item']] += d['amount']

print(counter)
