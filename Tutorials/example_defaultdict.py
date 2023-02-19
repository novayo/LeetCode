hash_table = {}

hash_table['a'] = []
hash_table['a'].append(1)

# hash_table['b'].append(1) # KeyError: 'b'


# ====================================== #

import collections
d = collections.defaultdict(list)
d['a'].append(1)
d['b'].append(1)
print(d) # defaultdict(<class 'list'>, {'a': [1], 'b': [1]}) <==> {'a': [1], 'b': [1]}
