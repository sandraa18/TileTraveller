#

start = 1.1

while start != 3.1 :

    if start == 1.1:
        valid_direction = "n"
        print("You can travel: (N)orth")
    elif start == 1.2:
        valid_direction = "nes"
        print("You can travel: (N)orth or (E)ast or (S)outh")
    elif start == 1.3:
        valid_direction = "es"
        print("You can travel: (E)ast or (S)outh")
    elif start == 2.1:
        valid_direction = "n"
        print("You can travel: (N)orth")
    elif start == 2.2:
        valid_direction = "ws"
        print("You can travel: (W)est or (S)outh")
    elif start == 2.3:
        valid_direction = "ew"
        print("You can travel: (E)ast or (W)est")
    elif start == 3.1:
        valid_direction = "n"
        print("You can travel: (N)orth")
    elif start == 3.2:
        valid_direction = "ns"
        print("You can travel: (N)orth or (S)outh")
    elif start == 3.3:
        valid_direction = "ws"
        print("YOu can travel: (W)est or (S)outh")

    direction = input("Direction: ")
    direction_lower = direction.lower()

    if direction in valid_direction:
        if direction == "n":
            start += 0.1
        elif direction == "e":
            start += 1
        elif direction == "s":
            start -= 0.1
        elif direction == "w":
            start -= 1
        print("{:.1f}" .format(start))
        start = int("{:.1f}" .format(start))
    else:
        print("Not a valid direction!")
else:
    print("Victory!")

