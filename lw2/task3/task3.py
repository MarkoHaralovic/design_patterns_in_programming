def mymax(iterable, key):
  max_x=max_key=None

  for x in iterable:

    if max_x is None and max_key is None: 
       max_x = x
       max_key = key(x)
    if key(x) > max_key:
       max_key=key(x)
       max_x = x

  return max_x

f = lambda x: len(x)

list_of_strings = ['a', 'b', 'c', 'd', 'e', 'efg','ijk','lmnnnn','snjcnsjcn','cs','scscs']

print(mymax(list_of_strings,f))