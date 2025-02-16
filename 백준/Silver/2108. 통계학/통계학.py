import sys

n = int(sys.stdin.readline().strip())
temp = sorted([int(sys.stdin.readline().strip()) for _ in range(n)])


sumi = round(sum(temp)/len(temp))
medii = temp[len(temp)//2]

dicti = {}
for i in temp:
    if i not in dicti:
        dicti[i] = 1
    else:
        dicti[i] += 1
        
maxi = max(dicti.values())
temp2 = [key for key, value in dicti.items() if value == maxi]
modei = temp2[1] if len(temp2) > 1 else temp2[0]


rangei = max(temp)-min(temp)

print(sumi, medii, modei, rangei, sep='\n')