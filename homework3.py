import random
n=int(input("Введите длину списка:\n"))
A=[]
for i in range(n):
	a=random.randint(1,99)
	A.append(a)
s=sum(A)
l=len(A)
a=s/l
print("Среднее арифметическое списка "+str(a))

