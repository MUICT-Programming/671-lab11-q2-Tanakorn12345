n = int(input())

l1 = []
l2 = []

for i in range (n):
    nn = int(input())
    l1.append(nn)

for i in range (n):
    nn = int(input())
    l2.append(nn)

def  summation(l1,l2):
    global n
    up = [0]*n
    for i in range(n):
      up[i] = l1[i] + l2[i]
    return up

def find_min_max(up):
    return min(up),max(up)

print(summation(l1,l2))
print(find_min_max(summation(l1,l2)))
