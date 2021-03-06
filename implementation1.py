#Upphafsstilla start sem 1.1
#Skilgreina hvaða áttir eru valid fyrir hvern stað
#passa að hafa átt bara sem lítinn staf, þ.e breyta í lítinn staf ef sleginn er inn stór stafur
#Finna út nýja gildi á start miðað við hvaða átt er slegin inn
#Halda áfram í while lykkju þangað til við erum komin á reit 3.1, þá er búið að vinna

#1. Which implementation was easier and why?
    #Myndi segja að fyrri gerðin hafi verið auðveldari af því að við erum búin að vera forrita meira þannig.
    #Meira sem þarf að hugsa og spá í þegar verið er að búa til föll
#2. Which implementation is more readable and why?
    #Seinna forritið, það með föllunum. Þá þarf ekki endalaust að skrifa það sama aftur og aftur.
    #Aðal kóðinn verður styttri og ef föllin eru með nógu lýsandi nöfnum þá ætti að vera skiljanlegt hvað er í gangi í hverju falli
#3. Which problems in the first implementations were you able to solve with the latter implementation?
    #Læsilegri kóði
    #Aðal kóðinn er styttri
    #Skiljanlegra fyrir aðra sem vilja skoða kóðann

def x_and_y(x,y):
    ''' Upphafsgildi á x og y '''
    return x,y

def Get_direction():
    '''Fá átt frá notanda'''
    a = input("Direction: ")
    a = a.lower()
    return a

def Get_valid_direction(a):
    '''Athuga hvaða áttir séu í boði fyrir hverja staðsetningu'''
    if a == 1:
        if start_y == 1:
            v_d = "n"
            print("You can travel: (N)orth.")
        elif start_y == 2:
            v_d = "nes"
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        elif start_y == 3:
            v_d = "es"
            print("You can travel: (E)ast or (S)outh.")
    elif a == 2:
        if start_y == 1:
            v_d = "n"
            print("You can travel: (N)orth.")
        elif start_y == 2:
            v_d = "ws"
            print("You can travel: (S)outh or (W)est.")
        elif start_y == 3:
            v_d = "ew"
            print("You can travel: (E)ast or (W)est.")
    elif a == 3:
        if start_y == 1:
            v_d = "n"
            print("You can travel: (N)orth.")
        elif start_y == 2:
            v_d = "ns"
            print("You can travel: (N)orth or (S)outh.")
        elif start_y == 3:
            v_d = "ws"
            print("You can travel: (S)outh or (W)est.")
    return v_d

def Get_new_x_and_y (d, x, y):
    '''Uppfæra gildi á x og y'''
    if d == "n":
        y += 1
    elif d == "e":
        x += 1
    elif d == "s":
        y -= 1
    elif d == "w":
        x -= 1    
    return x, y

def If_valid_direction(d, v, x, y):
    '''Athuga hvort átt sem slegin var inn sé í boði'''
    if d in v:
        x, y = Get_new_x_and_y(direction, start_x, start_y)    
    else:
        print ("Not a valid direction!")
        d = Get_direction()
        if d in v:
            x, y = Get_new_x_and_y(d, start_x, start_y)
    return x, y

    

start_x, start_y = x_and_y(1,1)

while start_x != 3 or start_y != 1 :
   
    valid_direction = Get_valid_direction(start_x)

    direction = Get_direction()

    start_x, start_y = If_valid_direction(direction, valid_direction, start_x, start_y)
else:
    print("Victory!")