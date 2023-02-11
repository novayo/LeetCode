a = [9]

# Change length
a.append(20)

# Change value
a[0] = 10

print(a) # [10,20]

# Cannot be hash
hash_table = {}
# hash_table[a] = 10 # TypeError: unhashable type: 'list'
