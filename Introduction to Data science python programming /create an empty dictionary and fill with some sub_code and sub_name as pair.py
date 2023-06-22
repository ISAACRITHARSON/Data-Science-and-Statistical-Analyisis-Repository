a = {}
n = int(input('Enter no.of.data to store in dictionary: '))
for i in range(n):
key = int(input('Enter subcode: '))
value = input('Enter subname: ')
a[key] = value
search = int(input('Enter subcode to search: '))
a[search]
