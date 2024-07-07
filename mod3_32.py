d = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 1, 'elderberry': 7}

print("Ascending order:", dict(sorted(d.items(), key=lambda item: item[1])))
print("Descending order:", dict(sorted(d.items(), key=lambda item: item[1], reverse=True)))
