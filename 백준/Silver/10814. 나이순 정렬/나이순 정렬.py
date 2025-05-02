
import sys
data = sys.stdin.readlines()[1:]
data.sort(key=lambda d : int(d.split()[0]))

print("".join(data))