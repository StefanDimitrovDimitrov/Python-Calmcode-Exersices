### comprehension - enumerate

print([char for ind, char  in enumerate('abcde') if ind % 2 == 0])

old_list = "abcde"
new_list = []
for i, c in enumerate(old_list):
    if i % 2 == 0:
        if c in 'aeuio':
            char = c.upper()
        else:
            char = c
        new_list.append(char)

print(new_list)

result = [c.upper() if c in 'aeuio' else c
          for i, c in enumerate(old_list)
          if i % 2 == 0]

print(result)


# two for loops with if statments

for i in range(5):
    if i > 2:
        for j in range(i):
            if j < 2:
                print((i, j))

print([(i, j) for i in range(5) if i > 2 for j in range(i) if j < 2])

# dict example

print({i: c for i, c in enumerate('abceabce') if i < 5})

print({c: i for i, c in enumerate('abcdefa')})
# we can lose information because we have twice key 'a'

# tuple
arr = [('a', 1),('b', 2),('c', 3),]
print([[key,value] for idx, (key, value) in enumerate(arr)])

print([{key: value, 'i': idx} for idx, (key, value) in enumerate(arr)])


# dict.values()

d = {'a': 1, 'b': 2, 'c': 3}
print([(k, v) for k, v in d.items()])

#zip

list_1 = [1, 1, 2, 3]
list_2 = [4, 5, 6, 2]

print([[a, b] for a, b in zip(list_1, list_2)])
print([(a, b) for a, b in zip(list_1, list_2)])

