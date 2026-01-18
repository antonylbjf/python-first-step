notes = [12, 15, 8, 19]
total = 0
for note in notes:
    total += note
moyenne = total / len(notes)

print("Moyenne :", moyenne)
if moyenne < 10:
    print("Insuffisant 😬")
elif moyenne < 14:
    print("Correct 👍")
else:
    print("Très bien 🚀")
