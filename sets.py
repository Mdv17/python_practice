# In sets no element apears twice or thrice but only once

# Create an empty set
s = set()

# Add elements to a set
# in sets you cant sort the order
s.add(1)
s.add(3)
s.add(4)
s.add(2)
s.add(3)

# Remove an element in set
s.remove(2)

print(s)
print(f"The set has {len(s)} elements")