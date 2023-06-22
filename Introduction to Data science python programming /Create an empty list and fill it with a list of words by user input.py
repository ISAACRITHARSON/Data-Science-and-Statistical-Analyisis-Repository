a = []
n = int(input('Enter no.of.data to store in list: '))
for i in range(n):
data = input('Enter data: ')
a.append(data)
m = int(input('Enter size: '))
for j in a:
if len(j)>m:
print(j)
