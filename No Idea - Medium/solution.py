## Taking and parsing all the inputs
n, m = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]
A = set([int(i) for i in input().split()])
B = set([int(i) for i in input().split()])


## The Actual Logic to solve the question
## This won't be the case for most questions

total = 0

for i in range(len(arr)):
    if arr[i] in A:
        total += 1
    if arr[i] in B:
        total -= 1
        
print(total)