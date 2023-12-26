# An anagram is nothing but when a string 's' consist of 't' string where characters are arranged in random order

s = "cat"
t = "nagaram"
dict1 = {}
dict2 = {}

for ch in s:
    j = 1
    if ch in dict1:
        dict1[ch] += 1
    else:
        dict1[ch] = 1
for ch in t:
    j = 1
    if ch in dict2:
        dict2[ch] += 1
    else:
        dict2[ch] = 1

print(dict2)

if dict1 == dict2:
    print("true")
else:
    print("false")

# another solution is to use

# return Counter(s) == Counter(t)

# # sorting

# s = "anagram"
# t = "nagaram"

# print(sorted(s) == sorted(t))
