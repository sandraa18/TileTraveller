#

start = 1.1
print("You can travel: (N)orth")
direction = input("Direction: ")
direction_upper = direction.lower()

while start != 3.1 :
    
    if direction == "n":
        start += 0.1
    else:
        print("Not a valid direction!")

else:
    print("Victory!")
    break
