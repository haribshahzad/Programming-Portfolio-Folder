import os
os.system("cls")

snacks=["Snickers", "Maltesers", "Pringles"]
print("This is the original list.")
print(snacks)
print("\nThis is the List in alphabetical order.")
print(sorted(snacks))
print("\nThis is the list in reverse alphabetical order.")
snacks.sort(reverse=True)
print(snacks)
print("\nThis is the original list.")
print(snacks)