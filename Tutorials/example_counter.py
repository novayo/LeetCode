hash_table = {}

hash_table['a'] = 0
hash_table['a'] += 1

# hash_table['b'] += 1 # KeyError: 'b'


# ====================================== #

import collections
counter = collections.Counter()
counter['a'] += 1
counter['b'] += 1
print(counter) # Counter({'a': 1, 'b': 1}) <==> {'a': 1, 'b': 1}
