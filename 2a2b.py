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
#print('ans=',ans)
while 1==1:
    guess = [int(s) for s in input('key 4 number:')]
    while len(guess) != 4:
        print("Please enter four digits")
        guess = [int(s) for s in input('key 4 number:')]
    for i in range(4):
        for j in range(4):
            if ans[i] == guess[j] and i==j:a+=1
            if ans[i] == guess[j] and i!=j:b+=1
    print(a,'A',b,'B')
    if a==4:
        print('yes ans is',*ans)
        break
    a=0
    b=0


