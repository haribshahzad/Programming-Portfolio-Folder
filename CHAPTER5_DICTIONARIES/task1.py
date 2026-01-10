student = {'name': 'Mark', 'marks': ['Codelab1 - 78', 'Codelab2 - 82']}

print(f"The student {student['name']} obtained the following marks:")
for mark in student['marks']:
    print("\t" + mark)