s={'a':10,'b':20,'c':30}
# add element
s.update({'d':40,'e':30,'f':30,'g':30})
print(s)

# pop last
s.popitem()
print(s)

# pop particular
s.pop('e')   #also prints the popped value
del s['c']  #doesnt print

# clear dict
s.clear()