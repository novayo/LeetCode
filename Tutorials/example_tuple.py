a = (10,20)

# Can not Change length
# a.append(1) # crash here

# Change value
# a[0] = 10 # TypeError: 'int' object does not support item assignment

print(a) # # (10,20)

# Cannot be hash
hash_table = {}
hash_table[a] = 99
print(hash_table) # {(10, 20): 99}