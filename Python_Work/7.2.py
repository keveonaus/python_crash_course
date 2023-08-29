seating = input("How many people are in you're party?: ")
seating = int(seating)

if seating >= 9:
    print("\nSorry you'll have to wait to be seated.")
else:
    print("\nYour table is ready!")