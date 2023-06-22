a = tuple()
l = list(a)
n = int(input('Enter no.of.data to store in tuple: '))
for i in range(n):
data = int(input('Enter data:'))
l.append(data)
a= tuple(l)
num = int(input('Enter num :'))
print(f"No.of.Occurences: {a.count(num)}")
