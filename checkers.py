pos=[9,9,9,9,9,9,9,9,9,9,0,1,0,1,0,1,0,1,9,9,1,0,1,0,1,0,1,0,9,9,0,1,0,1,0,1,0,1,9,9,0,0,0,0,0,0,0,0,9,9,0,0,0,0,0,0,0,0,9,9,2,0,2,0,2,0,2,0,9,9,0,2,0,2,0,2,0,2,9,9,2,0,2,0,2,0,2,0,9,9,9,9,9,9,9,9,9,9,9,9]

legalmoves=[11,13,15,17,29,22,24,26,31,33,35,37,40,42,44,46,51,53,55,57,60,62,64,66,71,73,75,77,80,82,84,86]

historyfrom[0]

historyto[0]

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
    
    requestinput=true
    while requestinput==true:
        movefrom=input("Move from: ")
        if movefrom in legalmoves and (pos[movefrom]==2 or pos[movefrom]==4):
            historyfrom.append[movenumber]
            requestinput=false
        else:
            print("This move is not legal.")

    requestinput=true
    while requestinput==true:
        moveto=input("Move to: ")
        if moveto in legalmoves:
            requestinput=false
        else:
            print("This move is not legal.")      
