#Upphafsstilla start sem 1.1
#Skilgreina hvaða áttir eru valid fyrir hvern stað
#passa að hafa átt bara sem lítinn staf, þ.e breyta í lítinn staf ef sleginn er inn stór stafur
#Finna út nýja gildi á start miðað við hvaða átt er slegin inn
#Halda áfram í while lykkju þangað til við erum komin á reit 3.1, þá er búið að vinna

start_x = 1
start_y = 1

while start_x != 3 or start_y != 1 :
    if start_x == 1:
        if start_y == 1:
            valid_direction = "n"
            print("You can travel: (N)orth.")
        elif start_y == 2:
            valid_direction = "nes"
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        elif start_y == 3:
            valid_direction = "es"
            print("You can travel: (E)ast or (S)outh.")
    elif start_x == 2:
        if start_y == 1:
            valid_direction = "n"
            print("You can travel: (N)orth.")
        elif start_y == 2:
            valid_direction = "ws"
            print("You can travel: (S)outh or (W)est.")
        elif start_y == 3:
            valid_direction = "ew"
            print("You can travel: (E)ast or (W)est.")
    elif start_x == 3 :
        if start_y == 1:
            valid_direction = "n"
            print("You can travel: (N)orth.")
        elif start_y == 2:
            valid_direction = "ns"
            print("You can travel: (N)orth or (S)outh.")
        elif start_y == 3:
            valid_direction = "ws"
            print("You can travel: (S)outh or (W)est.")

    direction = input("Direction: ")
    direction = direction.lower()

    if direction in valid_direction:
        if direction == "n":
            start_y += 1
        elif direction == "e":
            start_x += 1
        elif direction == "s":
            start_y -= 1
        elif direction == "w":
            start_x -= 1
    else:
        print("Not a valid direction!")
        direction = input("Direction: ")
        direction = direction.lower()
        if direction in valid_direction:
            if direction == "n":
                start_y += 1
            elif direction == "e":
                start_x += 1
            elif direction == "s":
                start_y -= 1
            elif direction == "w":
                start_x -= 1
else:
    print("Victory!")