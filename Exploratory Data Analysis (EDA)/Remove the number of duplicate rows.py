duplicate = t.duplicated().sum()
drop_duplicates = t.drop_duplicates()
print(f'There are {duplicate} duplicated rows in this table\nThe new table
is: ')
drop_duplicates
