alien_color=input("Enter Alien color:").lower()

if alien_color=="green":
    print("Player earned 5 Points")
elif alien_color=="yellow":
    print("Player earned 3 Points")
elif alien_color=="red":
    print("Player earned 2 Points")
else:
    print("Invalid color, Player earned 0 points")