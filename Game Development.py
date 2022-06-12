#Game Development: Snake Water Gun
i=10
comp = 0  # a is computer
user = 0  # b is snake
while i>=0:
    if i==0:
        print("The game has over")
        if comp>user:
            print("The computer has won")
            break
        elif comp<user:
            print("The user has won")
            break
        else:
            print("There is tie")
            break

    import random
    lst=("snake","water","gun")
    a=random.choice(lst)
    print("\n1.s=snake\n2.w=water\n3.g=gun")
    print("Enter the choice:")
    b=input()

    # This is for Snake and Water:
    if a=="snake" and b=="w":
        print("Snake drank water")
        comp=comp+1
        i=i-1
        print(f"computer:{comp} user:{user}")
        print(f"No. of turns left:",i)

    elif a=="water" and b=="s":
        print("Snake drank water")
        user=user+1
        i=i-1
        print(f"computer:{comp} user:{user}")
        print(f"No. of turns left:",i)

    # This is for Water and Gun:
    elif a=="water" and b=="g":
        print("Gun sinked in Water")
        comp=comp+1
        i=i-1
        print(f"computer:{comp} user:{user}")
        print(f"No. of turns left:",i)

    elif a == "gun" and b == "w":
        print("Gun sinked in Water")
        user=user+1
        i = i - 1
        print(f"computer:{comp} user:{user}")
        print(f"No. of turns left:", i)

    # This is for Gun and Snake:
    elif a=="gun" and b=="s":
        print("Gun killed Snake")
        comp=comp+1
        i =i-1
        print(f"computer:{comp} user:{user}")
        print(f"No. of turns left:",i)

    elif a=="snake" and b=="g":
        print("Gun killed Snake")
        user=user+1
        i=i-1
        print(f"computer:{comp} user:{user}")
        print(f"No. of turns left:",i)

    else:
        print("Error!You have got the same")
        print("Try Again!")
        i=i-1
        print(f"No. of turns left:",i)



