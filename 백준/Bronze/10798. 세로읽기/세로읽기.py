temp = []
string = ''

for _ in range(5):
    temp.append(input())

maxlen = max(len(i) for i in temp)

for i in range(maxlen):
    for query in temp: # query = AABCDD
        try: # trt except
            string += query[i]
        except:
            pass
print((string))