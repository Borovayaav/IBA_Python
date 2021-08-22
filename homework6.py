import random
n=int(input("Введите длину списка:\n"))
A=[]
for i in range(n):
	a=random.randint(-10,10)
	A.append(a)
print(A)
print(sum([i for i in A if i<0]))
try:
    ind=[i for i, x in enumerate(A) if x == 0]
    if len(ind)<=1:
        print("0")
    else:
        null1=ind[0]
        null2=ind[1]
        count=sum(A[null1:null2])
        print(count)
except ValueError:
    print("0")
