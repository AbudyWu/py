import random
from random import randint
a=0
b=0
print('start')
def generate():
    num = [0,1,2,3,4,5,6,7,8,9]
    random.shuffle(num)
    while num[0]==0:
        random.shuffle(num)
    result=num[:4]
    return result
ans = generate()
print('ans=',ans)
while 1==1:
    #guess = [int(s) for s in input('key 4 number:')]
    aa=input('key 4 number:')
    if len(aa) != 4 :
        print('\033[31;46m pls input 4 digit \033[0m')
        continue
    if str.isdigit(aa) == False :
        print('\033[31;46m pls input num \033[0m')
        continue
    if aa[0] == "0":
        print('\033[31;46m pls>1000 \033[0m')
        continue
    if len(set(aa))< 4 :
        print('\033[31;46m 不重複 \033[0m')
        continue
    guess = [int(s) for s in aa]
    for i in range(4):
        for j in range(4):
            # if ans[i] == guess[j] and i==j:a+=1
            # if ans[i] == guess[j] and i!=j:b+=1

            if ans[i] == guess[j]:
                if i == j:
                    a += 1
                else:
                    b += 1

    print(a,'A',b,'B')
    if a==4:
        print('\033[33;45m YES ANS IS :\033[0m',*ans)
        break
    a=0
    b=0