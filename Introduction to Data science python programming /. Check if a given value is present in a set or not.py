a = set()
n = int(input('Enter no.of.data to store in set: '))
for i in range(n):
data = input('Enter data:')
a.add(data)
b = input('Enter data to search: ')
if b in a:
print("Searched element: "+b)
