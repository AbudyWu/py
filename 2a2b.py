import random
from typing import List

def generate() -> List[int]:
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(num)
    while num[0] == 0:
        random.shuffle(num)
    result = num[:4]
    return result
def interactive() -> List[int]:
    while 1:
        user_ans = input("key 4 number:")
        if check(user_ans) == False:
            continue
        else:
            final = [int(s) for s in user_ans]
            return final
def game(x,y) -> bool:
    a = 0
    b = 0
    for i in range(4):
        for j in range(4):
            if x[i] == y[j]:
                if i == j:
                    a += 1
                else:
                    b += 1
    print(a, "A", b, "B")
    if a == 4:
        print("\033[33;45m YES ANS IS :\033[0m", *ans)
        return False
    return True
def check(aa) -> bool:
    if len(aa) != 4:
        print("\033[31;46m pls input 4 digit \033[0m")
        return False
    if str.isdigit(aa) == False:
        print("\033[31;46m pls input num \033[0m")
        return False
    if aa[0] == "0":
        print("\033[31;46m pls>1000 \033[0m")
        return False
    if len(set(aa)) < 4:
        print("\033[31;46m 不重複 \033[0m")
        return False
    else:
        return True

if __name__ == "__main__":
    key = True
    print("2A2B start!")
    ans = generate()
    print('ans=',ans)
    while key:
        guess = interactive()
        key=game(ans,guess)