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
    update_list = [0]*n
    for i in range(n):
      update_list[i] = l1[i] + l2[i]
    return update_list

def find_min_max(update_list):
    return min(update_list),max(update_list)

print(summation(l1,l2))
print(find_min_max(summation(l1,l2)))
