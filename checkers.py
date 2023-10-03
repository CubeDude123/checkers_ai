pos=[9,9,9,9,9,9,9,9,9,9,0,1,0,1,0,1,0,1,9,9,1,0,1,0,1,0,1,0,9,9,0,1,0,1,0,1,0,1,9,9,0,0,0,0,0,0,0,0,9,9,0,0,0,0,0,0,0,0,9,9,2,0,2,0,2,0,2,0,9,9,0,2,0,2,0,2,0,2,9,9,2,0,2,0,2,0,2,0,9,9,9,9,9,9,9,9,9,9,9,9]

legalmoves=[11,13,15,17,29,22,24,26,31,33,35,37,40,42,44,46,51,53,55,57,60,62,64,66,71,73,75,77,80,82,84,86]

historyfrom=[]

historyto=[]

def showboard():

    i=1

    for x in pos:
        if x==9:
           y='  '
        elif x==0:
            y='- '
        elif x==1:
            y='b '
        elif x==2:
            y='w '
        
        if i%10==0:
            print(y)
            i+=1 
        else:
            print(y,end='')
            i+=1
    
def moveinput(player, movenumber):
    
    if player=="white":
        requestinput="true"
        while requestinput=="true":
            movefrom=input("Move from: ")
            if movefrom in legalmoves and pos[movefrom]==2: #piece is man
                piece="man"
                if pos[movefrom-9]==0 or pos[movefrom-11]==0:
                    requestinput="false"
                else:
                    print("This piece does not have any legal moves.")
            elif movefrom in legalmoves and pos[movefrom]==4: #piece is king 
                if pos[movefrom-9]==0 or pos[movefrom-11]==0 or pos[movefrom+9]==0 or pos[movefrom+11]==0:
                    piece="king"
                    requestinput="false"
                else:
                    print("This piece does not have any legal moves.")
            else: #no white piece on this square
                print("You dont have a piece on this square.")

        requestinput="true"
        while requestinput=="true":
            moveto=input("Move to: ")
            if moveto in legalmoves:
                if piece=="man":
                    if (movefrom-9==moveto or movefrom-11==moveto) and pos[moveto]==0:
                        requestinput="false"
                    else:
                        print("Cant move to this square")
                elif piece=="king":
                    if kingmovable(movefrom,moveto)=="true": 
                        requestinput="false"
                    else:
                        print("Cant move to this square")
            else:
                print("This move is not legal.")      

    if player=="black":
        requestinput="true"
        while requestinput=="true":
            movefrom=input("Move from: ")
            if movefrom in legalmoves and pos[movefrom]==1: #piece is man
                piece="man"
                if pos[movefrom+9]==0 or pos[movefrom+11]==0:
                    requestinput="false"
                else:
                    print("This piece does not have any legal moves.")
            elif movefrom in legalmoves and pos[movefrom]==3: #piece is king 
                if pos[movefrom-9]==0 or pos[movefrom-11]==0 or pos[movefrom+9]==0 or pos[movefrom+11]==0:
                    piece="king"
                    requestinput="false"
                else:
                    print("This piece does not have any legal moves.")
            else: #no white piece on this square
                print("You dont have a piece on this square.")

        requestinput="true"
        while requestinput=="true":
            moveto=input("Move to: ")
            if moveto in legalmoves:
                if piece=="man":
                    if (movefrom+9==moveto or movefrom+11==moveto) and pos[moveto]==0:
                        requestinput="false"
                    else:
                        print("Cant move to this square")
                elif piece=="king":
                    if kingmovable(movefrom,moveto)=="true": 
                        requestinput="false"
                    else:
                        print("Cant move to this square")
            else:
                print("This move is not legal.")

def jump(jumpfrom,jumpto):

    #does the current player have to jump?
    print("")

def move(movefrom,moveto):

    #performing the move and logging it
    print("")

def kingmovable(movefrom, moveto):
    movediff=moveto-movefrom
    if movediff%9==0:
        mdiff=movediff/9
        for x in range(mdiff):
            if pos[moveto]!=0:
                movable="no" 
            else:
                movable="yes"   
        
    elif movediff%11==0:
        mdiff=movediff/11
        for x in range(mdiff):
            if pos[moveto]!=0:
                movable="no"
            else:
                movable="yes"

    else:
        movable="no"

    return movable