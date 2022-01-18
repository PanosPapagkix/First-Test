N=10
import random
randomlist = random.sample(range(1, 100), N)
L=randomlist

print("Αρχική Λίστα:",L)
for i in range(N-1):
    for j in range(N-i-1):
        if L[j+1]<L[j]:
            L[j],L[j+1]=L[j+1],L[j]
print("Ταξινομημένη Λίστα:",L)