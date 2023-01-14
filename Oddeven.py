def oddeven():
    choice=input("Enter Odd or Even: ")
    from random import randint
    l1=["Odd","Even"]
    l2=["Bat","Bowl"]
    l=randint(0,1)
    if l1[l]==choice:
        print("You won the toss")
        choice2=input("Bat or Bowl?: ")
    else:
        print("You lost the toss")
        l=randint(0,1)
        choice2=l2[l]
    print("You would ",choice2,"first")
    m=0
    n=0
    scorea=0
    scoreb=0
    out="false"
    if choice2=="Bat":
        print("Your batting")
        while out=="false":
            m=int(input("Enter a number: "))
            n=randint(1,6)
            print(n)
            if m==n:
                print("Out")
                out="true"
            else:
                scorea+=m
                print("score:",scorea)
        out="false"
        print("Second innings")
        while out=="false":
            m=int(input("Enter a number: "))
            n=randint(1,6)
            print(n)
            if m==n:
                print("Out")
                out="true"
            else:
                scoreb+=n
                print("score:",scoreb)
        if scorea>scoreb:
            print("You win")
        elif scoreb>scorea:
            print("You lost")
        else:
            print("It is a tie")
    elif choice2=="Bowl":
        while out=="false":
            m=int(input("Enter a number"))
            n=randint(1,6)
            print(n)
            if m==n:
                print("Out")
                out="true"
            else:
                scoreb+=n
                print("score:",scoreb)
        out="false"
        while out=="false":
            m=int(input("Enter a number"))
            n=randint(1,6)
            print(n)
            if m==n:
                print("Out")
                out="true"
            else:
                scorea+=m
                print("score:",scorea)
        print("Second innings")
        if scorea>scoreb:
            print("You win")
        elif scoreb>scorea:
            print("You lost")
        else:
            print("It is a tie")