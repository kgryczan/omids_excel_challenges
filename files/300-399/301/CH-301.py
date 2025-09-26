import random
p=[random.randint(1,10)]
for _ in range(4):
 p+=[random.choices(range(1,11),[2 if i==p[-1] else 1 for i in range(1,11)])[0]]
print(p)