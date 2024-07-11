heros=['spider man','thor','hulk','iron man','captain america']

print('Length of the list:',len(heros))
heros.append('black panther')
print('Added \'black panther\' at the end of this list')
print(heros)
heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)
heros[1:3]=['doctor strange']
print(heros)
print(dir(heros))
heros.sort()
print(heros)
