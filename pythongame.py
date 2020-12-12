print("Welcome to my first game")
name = input("Hi, what is you name?")
age = int(input("How old are you?"))

print("Hello", name,"you are", age, "years old")

health = 100 


if age >= 18:
    print("You are old enough to play")

    print("You are starting with", health, "points of health")

    wants_to_play = input ("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Let's play")

        left_or_right = input("First choice...Left or Right (left/right)?")
        if left_or_right == "left":
            ans = input("Nice, you follwed the path and reached a lake...Do you swim across or go around (across/around)?")

            if ans == "around":
                print("You went around and reached the other side of the lake")

            elif  ans == "across":
                print("You managed to get across, but you got hurt and lost 50 health")
                health -=50

            ans = input("You notice a house and a river. Which do you go to (river/house)? ")
            if ans == "house":
                print("You go to the house and get attacked by a bear, you survive but lose 10 points of health")
                health -= 10 

                if health <= 0:
                    print("You now have 0 health and you lose the game")
                else:
                    print("You have survived and have won the game!!!")

                
            else:
                print("You fell in the frozen river and lost the game... ")


           
        else:
            print("You fell down in a hole and lost the game")


    else:
        print("See ya later")


else: 
    print("You are too young to play")



