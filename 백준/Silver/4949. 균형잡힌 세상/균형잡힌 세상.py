import sys
from collections import deque

def sentence(words):
    words = words.replace(" ", "")

    num1 = 0
    num2 = 0
    temp = deque([])

    for i in words:
        if i in "()[]":
            if i == "[":
                num1 += 1
                temp.appendleft("[")
            elif i == "(":
                num2 += 1
                temp.appendleft("(")


            elif i == "]":
                num1 -= 1
                if (num1 < 0) or (temp[0] != "["):
                    return "no"
                else:
                    temp.popleft()                  
            elif i == ")":
                num2 -= 1
                if (num2 < 0) or (temp[0] != "("):
                    return "no"
                else:
                    temp.popleft()
                

        elif i == ".":
            if (num1 > 0) or (num2 > 0):
                return "no"
            else:
                return "yes"

while True:
    a = sys.stdin.readline().rstrip()
    if a == ".":
        break
    print(sentence(a))
    