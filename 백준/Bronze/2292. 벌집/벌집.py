n = int(input()) 
count = 1
bbox = 1

while bbox < n:
    bbox += 6*count
    count += 1

print(count)