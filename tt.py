import random
import operator
A=0
B=0
def checkB (list1,list2):
    B=0
    for a in list1:
        for b in list2:
            if a==b:
                B+=1
    return B

def checkA (list1,list2):
    A=0
    for i in range(4):
        if list1[i]==list2[i]:
            A+=1
    return A

list1=[0,1,2,3,4,5,6,7,8,9]
answer=random.sample(list1,4)
while answer[0]==0:
    answer=random.sample(list1,4)   
#print('answer=',answer)

while True:
    while 1:
        number=input('Please enter four numbers:')
        number=list(map(int,number))
        if len(set(number))==4: #& number[0]!=0:
            break
        else:
            print('\033[31mError\033[37m')
    if operator.eq(number,answer):
        print('Win')
        break
    else:
        B=checkB(number,answer)
        A=checkA(number,answer)
        B=B-A
        print(A,'A',B,'B')