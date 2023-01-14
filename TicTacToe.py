def tictactoe():
    class TicTacToe:
        def __init__(self):
            self.list1=[["_","_","_"],["_","_","_"],["_","_","_"]]
            self.movenumber=0
        def didWin(self):
            for i in self.list1:
                k=i[0]
                for j in i:
                    if j!=k:
                        break
                else:
                    return k
            for i in range(3):
                k=self.list1[0][i]
                for j in range(3):
                    if self.list1[j][i]!=k:
                        break
                else:
                    return k
            k=self.list1[1][1]
            if k==self.list1[0][0] and k==self.list1[2][2]:
                return k
            elif k==self.list1[2][0] and k==self.list1[0][2]:
                return k
            return "Draw"
        def Move(self,r,c,name):
            self.list1[r-1][c-1]=name
        def display(self):
            for i in self.list1:
                for j in i:
                    print(j,end=" ")
                print()

    C=TicTacToe()
    N1=input("Please enter the marker for player 1: ")
    N2=input("Please enter the marker for player 2: ")
    for i in range(9):
        r,c=[int(i) for i in input("Enter the coordinates of your move: ").split()]
        if i%2==0:
            C.Move(r,c,N1)
            C.display()
        elif i%2==1:
            C.Move(r,c,N2)
            C.display()
        K=C.didWin()
        if K==N1 or K==N2:
            print(K,"wins")
            break
    else:
        print("DRAW")