list = [2, 3, 5, 9, 3]
list_1 = []
index = (int(len(list)))
for i in range(index):
    if int(i) % 2 != 0:
        summa = 0
        summa = list[i] + summa
        list_1.append(summa)
    
print(list_1)



#print(sum(list[1::2]))