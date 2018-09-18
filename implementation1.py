#Upphafsstilla start sem 1.1
#Skilgreina hvaða áttir eru valid fyrir hvern stað
#passa að hafa átt bara sem lítinn staf, þ.e breyta í lítinn staf ef sleginn er inn stór stafur
#Finna út nýja gildi á start miðað við hvaða átt er slegin inn

start = 1.1

while start != 3.1 :

    if start == 1.1:
        valid_direction = "n"
        print("You can travel: (N)orth.")
    elif start == 1.2:
        valid_direction = "nes"
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif start == 1.3:
        valid_direction = "es"
        print("You can travel: (E)ast or (S)outh.")
    elif start == 2.1:
        valid_direction = "n"
        print("You can travel: (N)orth.")
    elif start == 2.2:
        valid_direction = "ws"
        print("You can travel: (S)outh or (W)est.")
    elif start == 2.3:
        valid_direction = "ew"
        print("You can travel: (E)ast or (W)est.")
    elif start == 3.1:
        valid_direction = "n"
        print("You can travel: (N)orth.")
    elif start == 3.2:
        valid_direction = "ns"
        print("You can travel: (N)orth or (S)outh.")
    elif start == 3.3:
        valid_direction = "ws"
        print("You can travel: (S)outh or (W)est.")

    direction = input("Direction: ")
    direction = direction.lower()

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
        start = round(start, 1)
    else:
        print("Not a valid direction!")
        direction = input("Direction: ")
        direction = direction.lower()
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
        start = round(start, 1)
else:
    print("Victory!")

