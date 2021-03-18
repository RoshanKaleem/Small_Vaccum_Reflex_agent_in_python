# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
S8 = ('B', 0, 0,)
S6 = ('B', 0, 1, S8)
S3 = ('A', 0, 1, S6)
S1 = ('A', 1, 1, S3)


S7 = ('A', 0, 0,)
S5 = ('A', 1, 0, S7)
S4 = ('B', 1, 0, S5)
S2 = ('B', 1, 1, S4)



print('Enter Room:(A or B)')
room = input()
print('Enter condition of room A(0/1 : clean/dirty):')
roomconditionA = int(input())
print('Enter condition of room B(0/1 : clean/dirty):')
roomconditionB = int(input())
cost=0



if (S8[0] == room and S8[1] == roomconditionA and S8[2] == roomconditionB):
    print("S8:-->Goal state:Both rooms are cleaned ")


if (S6[0] == room and S6[1] == roomconditionA and S6[2] == roomconditionB):
    print("S6:-->Vaccum in room B")
    cost = cost + 1
    print("S6:-->Trash sucked from room B ->cost:" + str(cost))



    if (S6[3][0] == 'B' and S6[3][1] == 0 and S6[3][2] == 0):
        print("S8:-->Goal state:Both rooms are now cleaned ")



if (S3[0] == room and S3[1] == roomconditionA and S3[2] == roomconditionB):
    print("S3:Room A is  cleaned")
    cost = cost + 1
    print("S3:Moving to room B ->cost:" + str(cost))



    if (S3[3][0] == 'B' and S3[3][1] == 0 and S3[3][2] == 1):
        print("S6:-->Vaccum in room B")
        cost = cost + 1
        print("S6:-->Trash sucked from room B ->cost:" + str(cost))


        if (S3[3][3][0] == 'B' and S3[3][3][1] == 0 and S3[3][3][2] == 0):
            print("S8:-->Goal state:Both rooms are now cleaned ")



if(S1[0]==room and S1[1]==roomconditionA and S1[2]==roomconditionB):
    print("S1-->Vaccum in room A")
    print("S1:Room A is not cleaned")
    print("S1:Room B is not cleaned")

    cost = cost + 1
    print("S1:-->Trash sucked from room A ->cost:" + str(cost))

    if(S1[3][0]=='A' and S1[3][1]==0 and S1[3][2]==1):
        print("S3:Room A is now cleaned")
        cost = cost + 1
        print("S3:Moving to room B ->cost:" + str(cost))


        if (S1[3][3][0] == 'B' and S1[3][3][1] == 0 and S1[3][3][2] == 1):
            print("S6:-->Vaccum in room B")
            cost = cost + 1
            print("S6:-->Trash sucked from room B ->cost:" + str(cost))


            if (S1[3][3][3][0] == 'B' and S1[3][3][3][1] == 0 and S1[3][3][3][2] == 0):
                print("S8:-->Goal state:Both rooms are now cleaned ")





if (S7[0] == room and S7[1] == roomconditionA and S7[2] == roomconditionB):
    print("S7:-->Goal state:Both rooms are cleaned ")



if (S5[0] == room and S5[1] == roomconditionA and S5[2] == roomconditionB):
    print("S5:-->Vaccum in room A")
    cost = cost + 1
    print("S5:-->Trash sucked from room A ->cost:" + str(cost))


    if (S5[3][0] == 'A' and S5[3][1] == 0 and S5[3][2] == 0):
        print("S7:-->Goal state:Both rooms are now cleaned ")



if (S4[0] == room and S4[1] == roomconditionA and S4[2] == roomconditionB):
    print("S4:Room B is cleaned")
    cost = cost + 1
    print("S4:Moving to room A ->cost:" + str(cost))


    if (S4[3][0] == 'A' and S4[3][1] == 1 and S4[3][2] == 0):
        print("S5:-->Vaccum in room A")
        cost = cost + 1
        print("S5:-->Trash sucked from room A ->cost:" + str(cost))


        if (S4[3][3][0] == 'A' and S4[3][3][1] == 0 and S4[3][3][2] == 0):
            print("S7:-->Goal state:Both rooms are now cleaned ")



if(S2[0]==room and S2[1]==roomconditionA and S2[2]==roomconditionB):
    print("S2-->Vaccum in room B")
    print("S2:Room A is not cleaned")
    print("S2:Room B is not cleaned")
    cost = cost + 1
    print("S5:-->Trash sucked from room B ->cost:" + str(cost))

    if(S2[3][0]=='B' and S2[3][1]==1 and S2[3][2]==0):
        print("S4:Room B is now cleaned")
        cost = cost + 1
        print("S4:Moving to room A ->cost:" + str(cost))


        if (S2[3][3][0] == 'A' and S2[3][3][1] == 1 and S2[3][3][2] == 0):
            print("S5:-->Vaccum in room A")
            cost = cost + 1
            print("S5:-->Trash sucked from room A ->cost:" + str(cost))


            if (S2[3][3][3][0] == 'A' and S2[3][3][3][1] == 0 and S2[3][3][3][2] == 0):
                print("S7:-->Goal state:Both rooms are now cleaned ")


print("Performance measuremnet "+str(cost)+"")

