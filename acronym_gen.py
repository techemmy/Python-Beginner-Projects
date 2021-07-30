term = input('Enter the term').replace('of', '').split()
acronym = ''.join([i[0].upper() for i in term])
print(acronym)