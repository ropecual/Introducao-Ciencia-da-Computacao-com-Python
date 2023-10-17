def busca(seq, x):
    '''(list, float) -> bool'''
    for i in range(len(seq)):
        if seq[i] == x:
            return i
    return False



#print(busca(['a', 'e', 'i'], 'e'))
# deve devolver => 1

#print(busca([12, 13, 14], 15))
# deve devolver => False