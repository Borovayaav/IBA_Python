p=int(input("Введите выручку за первый день:"))
q=int(input("Введите желаемую выручку:"))
d=1
while p<=q:
	p*=1.03
	d+=1
print("Выручка, превысившая значение, соcтавила "+str(int(p*1.03))+" тысяч рублей")
print("Количество дней для достижения результата "+str(d+1))
