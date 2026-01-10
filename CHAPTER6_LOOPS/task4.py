orders = ['Wedding Bouquets', 'Birthday Bouquets', 'Party Bouquets', 'Rose Bouquets']
completed = []

while orders:
    item = orders.pop(0)
    print("I'm preparing your " + item + ".")
    completed.append(item)

print()

for item in completed:
    print("I made a " + item + ".")
